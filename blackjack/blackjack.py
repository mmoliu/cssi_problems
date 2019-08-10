import random

#drawing card, adding, comparing
def blackjack(score, dScore, PLAY, cards, MAX_NUMBER):
    print("Score: "+ str(score))
    print("Dealer: " + str(dScore))
    playerInput = raw_input("Would you like to draw a card? ")
    if playerInput.lower() == "yes" or playerInput.lower() == "y":
        randNum = random.randint(0, len(cards)-1)
        print("You drew a: " +str(cards[randNum]))
        if cards[randNum] == 'A':
            score+= 11
        else:
            score+= int(cards[randNum])
        del cards[randNum]
    else:
        print("You ended with score: " + str(score))
        PLAY = False
    if score > 21 and PLAY == True:
        print("Score: "+ str(score))
        print("Oof... you lost ")
        PLAY = reset()
    elif score == 21:
        print("Score: "+ str(score))
        print("You won!!! Good job!!!!!")
        PLAY = reset()
    if PLAY == True:
        blackjack(score, dScore, PLAY, cards, MAX_NUMBER)

#event flow, allows for reset
def reset():
    playerInput2 = raw_input("Would you like to play again?")
    if playerInput2.lower() == "yes" or playerInput2.lower() == "y":
        score = 0
        dScore = 0
        return True
    else:
        return False

#main, initialization of variables
def play_blackjack():
    score = 0
    dScore = 0
    PLAY = True
    cards = ['A', 'A', 'A', 'A', '2', '2','2','2','3','3','3', '3', '4', '4','4', '4','5','5', '5', '5', '6', '6','6','6','7','7', '7', '7', '8', '8', '8', '8', '9','9','9','9','10','10', '10', '10', '10','10', '10', '10', '10','10', '10', '10', '10','10', '10', '10' ]
    MAX_NUMBER = 21
    blackjack(score, dScore, PLAY, cards, MAX_NUMBER)

play_blackjack()
