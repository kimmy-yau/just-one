
from Game import playGame, printRules, setupPlayers
import pyinputplus as pyip

print("\nWelcome to Just One Game!")
print("\nThis game is suitable for a group of 4-8 players.")

activeSession = True

# Player Setup
players = setupPlayers()

while(activeSession):
    option = pyip.inputMenu(["Start","Rules","Exit"], prompt="Select one of the following options: \n", numbered = True)

    #Game Session
    if(option == "Start"):
        start = True
        while(start):
            start = playGame(players)
    elif(option == "Rules"):
        printRules()
    else:
        activeSession = False
        print("\nThank you for playing! Bye! ^^")
