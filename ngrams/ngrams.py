import random
import collections
import operator

def read_process_data():
    with open('mobydick.txt') as f:
        # - converts everything to lowercase, replaces newlines etc.
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower().split(" ")
        content =list(filter(lambda a: a != '', content))
        return content

def seedMap(content, num):
    map = {}
    window = [] #current words looking at
    lenWords = len(content)
    #creates an initial window
    for word in range(int(num)):
        window.append(content[word])
    # print(words)
    #select next word
    for i, word in enumerate(content):
        #print("i: " + str(i))
        newIndex = tuple(window)
        if newIndex not in map:
            map[newIndex] = [content[(num + i)%lenWords]] #gets the next word as a value for the key #e.g. {to, be} = {or}

        #if its already in it, add to the list
        elif newIndex in map:
            map[newIndex].append(content[(num + i)%lenWords])

    #populate map with new window
        del window[0]
        window.append(content[(num + i)%lenWords])
    return map

def generateSentences(seedNum, numWords):
    content = read_process_data()
    sentence = ""
    window = []
    seedStart = random.randint(0,len(content))
    map = seedMap(content, seedNum)

#generate these sentences
#initializing first window
    for word in range(seedStart, seedStart+seedNum):
        window.append(content[word%len(content)])


#add next most freq window
    for i in range(0, numWords):
        index = tuple(window)
        ctr = collections.Counter(map[index]) #returns a dictionary from the list of items
        sentence = sentence + " " + str(max(ctr.iteritems(), key=operator.itemgetter(1))[0])
        #print(sentence)
        nextWord = seedStart+seedNum+i
        window.append(content[nextWord])
        del window[0]

    print(sentence)

seedNum = int(raw_input("Please pick a number for the seed: "))
numWords = int(raw_input("Number of words you want generated: "))

generateSentences(seedNum, numWords)
