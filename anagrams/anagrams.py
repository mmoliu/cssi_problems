
import collections
big_list = []
def read_process_data():
    with open('dict1.txt') as f:
        # processes data, replaces new lines w spaces, lowercases all, etc.
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower().strip(' ')
        content = content.split()
        return content

def LetterInventory(s): # s is the anagram
    s =s.strip(' ').lower()
    a= list(s) # creates a list of each of the characters
    return a

def isPrefix(prefix, dict):    #if any word in dict starts with prefix
   start=0
   end=len(dict)-1
   #binary search for the prefix
   while start<=end:
       mid=(start+end)/2
       curr=dict[mid]
       if len(prefix)<=len(curr) and curr[:len(prefix)]==prefix:
           return True
       elif prefix < curr:
           end=mid-1
       else:
           start=mid+1
   return False

def remove_char(string, char): #bush
    l = []
    l = list(string)
    l.remove(char)
    s =""
    for i in range(len(l)):
        s+= l[i]
    return s


def findAnagrams(commit, prefix, suffix, content):
    global big_list
    flag = isPrefix(prefix, content)
    print(prefix, suffix)
    if prefix == "" and suffix == "":
        if commit not in big_list: #commit is the first word you commit to
            big_list.append(commit)
        return
    if flag == False:
        return
    if prefix in content:

        findAnagrams(commit+[prefix], "", suffix, content)
    for i in range(len(suffix)):
        # findAnagrams(commit, prefix+char, remove_char(suffix, char), content)
        findAnagrams(commit,prefix+suffix[i],suffix[:i]+suffix[i+1:],content)


def main():
    anagram = raw_input()
    global big_list
    content = read_process_data()
    for i in range(len(anagram)):
        findAnagrams([], anagram[i], anagram[:i] + anagram[(i+1):], content)
    print(big_list)

main()

# def isPrefix(prefix, dictionary):
#     return isPrefix(prefix, dictionarym, start, end)

# def createFreq(list):
#     freq = [None] * 26
#     for letter in list:
#         freq[int(letter)] += 1
#     return freq





# def anagramSolver(s, dictionary):
#      # not supposed to use global variables
#     l = LetterInventory(s)
#     ctr = collections.Counter(l)``
#     # ['b', 'a','n', 'a']
#     wordLetter = createFreq(l) #[0, 2]
#     for word in content:


    #while there are still values in

#    for key in ctr:
#        if ctr[key] ==0:
#
#        prefix += "key"
#        ctr[key] -= 1
#        for

    # isPrefix()
    # workingString = ""

        #search for this in the dictionary


# def isPrefix(s, dictionary, start, end):
#     while start <= end:
#         if len(dictionary)%2:
#             middle = len(dictionary/2)-1
#         else:
#             middle = (len(dictionary)-1)/2
#         if prefix == dictionary[middle]:
#             # if prefix == dictionary[middle]:
#             #     big_list.append(prefix)
#             return True
#         elif prefix > dictionary[middle]:
#             start = middle +1
#         elif prefix < dictionary[middle]:
#             end = middle -1
#         isPrefix(prefix, dictionary, start, end)



    # letter.lower()
    # if (letter < 'a' or letter > 'z'):
    #     return 0
    # else:
    #     return coun
