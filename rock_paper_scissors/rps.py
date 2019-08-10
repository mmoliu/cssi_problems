PLAY = True
import random
scorep1 = 0
scorep2 = 0
scoreplayer =0
rocks = ["rock", "r", "rockko", "rck"]
scissors = ["scissors", 's', 'scors']
papers = ["p", "paper"]
tied = "Y'all tied... Want to play again?"
no = ["no", "n", "nah","yo no", "never"]
yes = ["yes","yeet", "ya", "yeah"]

while PLAY == True:

    compRPS = ["rock", "paper", "scissors"]
    comp_human = raw_input("Do you want to play against a computer or a human? ")
    if comp_human.lower() == "computer" or comp_human.lower() == "comp" or comp_human.lower() == "c":
        PLAY = True
        p1 = raw_input("Player, please enter rock paper or scissors ")
        compNum= random.randint(0,2) #0 = rocks, 1 = pap 2= scissors
        playingComp = "Computer played: " + compRPS[compNum]
        if compNum ==0 and (p1.lower() in rocks): #rocks, rocks
            print(playingComp)
            print(tied)
        elif (p1.lower() in scissors) and compNum ==0: #scissos, rock
            print(playingComp)
            print("CPU wins today :(")
        elif (p1.lower() in papers) and compNum ==0: #paper, rock
            print(playingComp)
            print("Yay!!! You win!!!")
            scoreplayer+=1;
        elif compNum ==1 and p1.lower() in scissors: #paper, scissors
            print(playingComp)
            print("CPU wins today :(")
        elif  compNum ==1 and (p1.lower() in rocks): #paper, rock
            print(playingComp)
            print("CPU won!!")
        elif compNum ==1 and (p1.lower() in papers): #paper paper
            print(playingComp)
            print(tied)
        elif compNum ==2 and (p1.lower() in scissors):
            print(playingComp)
            print(tied)
        elif compNum ==2 and (p1.lower() in rocks):
            print(playingComp)
            print("Congrats you win!!!")
            scoreplayer+=1;
        elif compNum ==2 and (p1.lower() in papers):
            print(playingComp)
            print("CPU wins today")
        else:
            print "Please check your spelling then try again :D"
        print ("Your score: %s" % (scoreplayer))
        answ = raw_input("Do you want to play again?")
        if answ in no:
            break
        else:
            continue
    elif comp_human.lower() == "human" or comp_human.lower() =="h" or comp_human.lower() == "man":
        PLAY = True
        p1 = raw_input("Player 1, please enter rock paper or scissors ")
        p2 = raw_input("Player 2, please enter rock paper or scissors ")
        if (p1.lower() in rocks) and (p2.lower() in scissors): #rocks scissors
            print("Player 1 won!")
        elif (p1.lower() in scissors) and (p2.lower() in scissors): #paper scissors
            print(tied)
        elif (p1.lower() in papers) and (p2.lower() in scissors): #sci sci
            print("Player 1 won!")
        elif (p2.lower() in rocks) and (p1.lower() in scissors): #
            print("Player 2 won!")
        elif (p2.lower() in rocks) and (p1.lower() in papers):
            print("Player 1 won!!")
        elif (p2.lower() in rocks) and (p1.lower() in scissors):
            print("Player 1 won :0")
        elif (p2.lower() in rocks) and (p1.lower() in rocks):
            print(tied)
        elif (p2.lower() in papers) and (p1.lower() in papers):
            print(tied)
        elif (p2.lower() in papers) and (p1.lower() in scissors):
            print("Player 1 won!")
        elif (p2.lower() in papers) and (p1.lower() in rocks):
            print("Player 2 won :0")
        else:
            print "Please check your spelling then try again :D"
        print ("P1 score: %s \n P2 score: %s" % (scorep1, scorep2))
        answ = raw_input("Do you want to play again? ")
        if answ in no:
            break
        else:
            continue
    elif comp_human in no:
        PLAY = False
    else:
        print "You didn't type in computer or human... please try again"
