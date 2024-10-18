from Player import Player
import time
import pyinputplus as pyip
from wonderwords import RandomWord

def setupPlayers():
    players = []
    numPlayers = pyip.inputInt("\nPlease enter the number of players: ", min=4,max=8)
    for playerNum in range(numPlayers):
        playerName = pyip.inputStr(f"\nPlease enter the name for Player {playerNum + 1}: ")
        players.append(Player(playerNum + 1, playerName))   
    
    return players

def playGame(players):
    points = 0

    #Each player takes turn being the Lead Detective.
    for player in players:
        duplicateHints = set()
        allHints = []
        print("\n"+player.playerName+ " will be the Lead Detective. Please look away.")
        time.sleep(3)
        print("\nChoosing a random word ...")
        r = RandomWord()
        word = r.word(include_parts_of_speech=["nouns"])
        print("****************************")
        print("****************************")
        print(f"The word is {word}")
        print("****************************")
        print("****************************")

        assistantTeam = players.copy()
        assistantTeam.remove(player)

        #Each Assistant takes turn typing their clue.
        for assistant in assistantTeam:

            print("****************************")
            print("****************************")
            print("****************************")
            print("****************************")
            hint = str.lower(pyip.inputStr(f"\n{assistant.playerName} - Enter one word hint: ", strip = True))
            print("****************************")
            print("****************************")
            print("****************************")
            print("****************************")
            if(not allHints.__contains__(hint) and not duplicateHints.__contains__(hint)):
                allHints.append(hint)
            else:
                if(allHints.__contains__(hint)):
                    allHints.remove(hint)
                duplicateHints.add(hint)
                        
        print("\nLead Detective, here are your clues:")
        
        for index,givenHint in enumerate(allHints, start=1):
            print(f"\n{index}. {givenHint}")

        guess = str.lower(pyip.inputStr("\nState your answer: ", strip = True))
                            
        if(guess == word):
            print("\nYay! You guessed it correctly!")
            points+=1
        else:
            print(f"\nOh no! That wasn't right! The Mystery word was {word}")

    print(f"\nTeam Score: {points}!")

    retry = pyip.inputYesNo("\nDo you want to play again (Y/N)? ",yesVal='Y', noVal='N', caseSensitive=False)
    if(retry == "Y"):
        return True
    else:
        return False

def printRules() : 
    print()
    print("****************************")
    print("******* Objective **********")
    print("****************************")
    print("\nYou are a team consisting one Lead Detective and the rest are Assistants. The Lead Detective has one attempt to guess the Mystery word correctly using the Assistants' clues.")
    
    print()
    print("****************************")
    print("******* How to Play ********")
    print("****************************")
    print("\nEach player will take turns as the Lead Detective. A random Mystery word will be generated. Other players (the Assistants) must type a ONE word clue that is related to the Mystery word.")
    print("\nThe detectives cannot see each other's answers.")
    print("\nAny clues that match will be discarded!")
    print("\nThe clue word cannot contain any parts of the Mystery word.")
    print("\nProper nouns are allowed but must be ONE word.")
    
    print()
    print("****************************")
    print("********* Example **********")
    print("****************************")
    print("\nPlayer 1 is the Lead Detective. ")
    print("The mystery word is crossroad.")
    print("Player 2 types intersection.")
    print("Player 3 types junction.")
    print("Player 4 types chicken. (IYKYK)")
    print("With the clues given, Player 1 guesses crossroad.")
    print("The team then earns one point.")
    
    print()
    print("****************************")
    print("*********** Tip ************")
    print("****************************")
    print("\nThink outside of the box! Hint word can be obscure but relatable - See Example")
    print("\nGood luck!")