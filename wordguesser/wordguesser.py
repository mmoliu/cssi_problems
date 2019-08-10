import random
from collections import Counter

#imports and processes list of all english wordguesser
def read_process_data():
    with open('words_alpha.txt') as f:
        # - converts everything to lowercase, replaces newlines etc.
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower().split(" ")
        content =list(filter(lambda a: a != '', content))
        return content

#creates the empty spaces
def spaceArray(length):
    a = []
    for i in range(length):
        a.append('_ ')
    return a

#loads the array each time
def loadArray(guessArray, guessString):
    for i in range(len(guessArray)):
        guessString += guessArray[i]
    return guessString

def findAnswer(guessArray, guessString, word):
    FOUND_ANSWER = False
    ctr= Counter(word)
    while FOUND_ANSWER == False:
        key = raw_input("Please guess a letter! ")
        if key in ctr:
            start = 0
            del ctr[key]
            for letter in word:
                if key == letter:
                    location = word.index(letter,start)
                    guessArray[location] = key
                    start = start+ word.index(letter) + 1
            print("Yes that is in this word!")
            print(loadArray(guessArray, guessString))
        elif key not in ctr:
            print("Dang man. It's not in there. try again! ")
        if ctr == Counter():
            print("You won!! won!! I am so proud of you!")
            FOUND_ANSWER = True

def wordguesser():
    #initializing words/variables
    words = read_process_data()
    guessArray = []
    guessString = ""
    listWord = []
    #possible options for what could be entered for player input
    computer = ["comp", "c", "computer", "cpu", "not human"]
    human = ["player", "human", "h", "p", "man", "person"]

    playerInput = raw_input("Would you like to play against a CPU or a friend? ")
    if playerInput.lower() in computer:
        randNum = random.randint(0, len(words)-1)
        word = words[randNum]
        for i in word:
            listWord.append(i)
        guessArray = spaceArray(len(words[randNum]))
        print(loadArray(guessArray, guessString))
        findAnswer(guessArray, guessString, listWord)
    elif playerInput.lower() in human:
        answer = raw_input("Player 1, please pick a word for the second player to guess ")
        guessArray = spaceArray(len(answer))
        print(loadArray(guessArray, guessString))
        findAnswer(guessArray, guessString, answer)

wordguesser()

#extensions: - have certain amount of chances - when guessing letter, put a list of letters already guessed - edge cases for what the player might input 
