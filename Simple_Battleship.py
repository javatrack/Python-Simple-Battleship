# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:56:32 2022

@author: Tristan
"""
#######################################################################   
# Program Filename:   FinalProject(date)
# Author:    Tristan Coffin
# Date:  6/7/2022
# Description:  A text based battleship game
# Input:  user inputs for position and direction
# Output:   winner
####################################################################### 

#%%
import numpy as np
rng = np.random.default_rng()

#%%
print("This is a battleship game. The enemy will be an AI with no adaptive moves.\n")
MsgPlaceShip = "Place your battleships"
MsgPl = "Place your "

#%% 
#score function keeps score
#######################################################################  
# Function:   scoreFuncP
# Description:  Keeps the AIs score counter intuitivly because I named based on which board they checked
# Parameters:   The board state of the Player board
# Return values:  Score for the AI
# Pre-Conditions:  Player exists
# Post-Conditions:   None?
####################################################################### 
def scoreFuncP():
    score = 0
    for x in range(0, len(Player)):
        if Player[x] == 1:
            score = score + 1
        else:
            pass
    return score

#######################################################################  
# Function:   scoreFuncAI
# Description:  Keeps player score
# Parameters:   AI
# Return values:  Score for player
# Pre-Conditions:  AI
# Post-Conditions:   
####################################################################### 
def scoreFuncAI():
    score = 0
    for x in range(0, len(AI)):
        if AI[x] == 1:
            score = score + 1
        else:
            pass
    return score



#%%
#This is the position returning function
#establishes the rows that will be used in the game
Arow = 0
Brow = 10
Crow = 20
Drow = 30
Erow = 40
Frow = 50
Grow = 60
Hrow = 70
Irow = 80
Jrow = 90

#######################################################################  
# Function:   position
# Description:  allows for the player to input positions using the classic battleship grid style
# Parameters:   letter input between A and J and number input between 1 and 10
# Return values:  position converted to 0 to 99 format
# Pre-Conditions:  none
# Post-Conditions:   none
####################################################################### 
def position():
    x = 0
    while x == 0:
        while True:
            try:
                row = input("Please input row (letter A-J): ")
                col = int(input("Please input column (Number 1-10): "))
                break
            except ValueError:
                print("Please follow the proper formats")
        if (col >= 1 and col <= 10):
            x = 1
        else:
            x = 0
            print("Please follow the column format")
        if row == "A":
            row = Arow
            x = 1
        elif row == "B":
            row = Brow
            x = 1
        elif row == "C":
            row = Crow
            x = 1
        elif row == "D":
            row = Drow
            x = 1
        elif row == "E":
            row = Erow
            x = 1
        elif row == "F":
            row = Frow
            x = 1
        elif row == "G":
            row = Grow
            x = 1
        elif row == "H":
            row = Hrow
            x = 1
        elif row == "I":
            row = Irow
            x = 1
        elif row == "J":
            row = Jrow
            x = 1
        else:
            x = 0
            print("Please follow the row format")
    pos = (row + col) - 1
    return pos
    

#test = position()
#print(test)

#%%
#ship placement options function
# Checks which options for a placement are valid and will stay on the board
#######################################################################  
# Function:   PlacementOptions
# Description:  Creates list of valid directions to face a ship once the initial spot is chosen
# Parameters:   inital placement and the length or "size" of the ship
# Return values:  Dictionary of valid places because this was easier to debug but it could be changed to an array
# Pre-Conditions:  placement exists size exists
# Post-Conditions:   none
####################################################################### 
def PlacementOptions(Placement, size):
    optionDic = {}
    opt1 = Placement - 10 * (size - 1)
    if opt1 < 0 or opt1 > 100:
        pass
    else:
        optionDic[0] = opt1
    opt2 = Placement + (size - 1)
    opt2fix = (Placement - ((Placement // 10) * 10)) + (size -1)
    if opt2fix < 0 or opt2fix > 9:
        pass
    else:
        optionDic[1] = opt2
    opt3 = Placement + 10 * (size - 1)
    if opt3 < 0 or opt3 > 100:
        pass
    else:
        optionDic[2] = opt3
    opt4 = Placement - (size - 1)
    opt4fix = (Placement - ((Placement // 10) * 10)) - (size -1)
    if opt4fix < 0 or opt4fix > 100:
        pass
    else:
        optionDic[3] = opt4
    return optionDic


#%%
# Creates a list of options from the directions for the player to place their ship
#######################################################################  
# Function:   optlist
# Description:  gets the player to chose the direction of the placement for a ship
# Parameters:   the placementoptions function works and a placement and size are given
# Return values:  the chosen output
# Pre-Conditions:  same as parameters
# Post-Conditions:   
####################################################################### 
def optlist(Placement, Size):
    optionsList = []
    option = PlacementOptions(Placement, Size)
    if 0 in option:
        optionsList.append(0)
    if 1 in option:
        optionsList.append(1)
    if 2 in option:
        optionsList.append(2)
    if 3 in option:
        optionsList.append(3)
    while True:
        print("Input the direction you wish to have your ship go from the list provided.")
        print("1 is up. 2 is right. 3 is down. 4 is left")
        printList = []
        for x in range(0, len(optionsList)):
            printList.append(optionsList[x] + 1)
        print(printList)
        while True:
            try:
                ChoseOpt = int(input("Number Chosen: "))
                break
            except ValueError:
                pass
        if ChoseOpt in printList:
            break
        else:
            pass
    return ChoseOpt

#%%
# the ai version of the options list function
#######################################################################  
# Function:   AIoptlist
# Description:  options list but for the AI
# Parameters:   nothing other than random values
# Return values:  the options chosen by the AI
# Pre-Conditions:  none
# Post-Conditions:   something accepts the output
####################################################################### 
def AIoptlist(Placement, Size):
    optionsList = []
    option = PlacementOptions(Placement, Size)
    if 0 in option:
        optionsList.append(0)
    if 1 in option:
        optionsList.append(1)
    if 2 in option:
        optionsList.append(2)
    if 3 in option:
        optionsList.append(3)
    while True:
        printList = []
        for x in range(0, len(optionsList)):
            printList.append(optionsList[x] + 1)
        while True:
            try:
                ChoseOpt = rng.integers(low = 1, high = 5, size = 1)
                break
            except ValueError:
                pass
        if ChoseOpt in printList:
            break
        else:
            pass
    return ChoseOpt



#%%
#Makes array for each spot the ship will take
#######################################################################  
# Function:   shipCheck
# Description:  checks how big the ship is and makes all the spaces it would take up are in one array
# Parameters:   size, the direction and the initial placement location
# Return values:  an array with the locations the ship will take
# Pre-Conditions:  a ship with a size a location and one of four directions
# Post-Conditions:   something to store the array
####################################################################### 
def shipCheck(Placement, size, Option):
    Attach = []
    if Option == 1:
        OptVar = -10
    elif Option == 2:
        OptVar = 1
    elif Option == 3:
        OptVar = 10
    elif Option == 4:
        OptVar = -1
    for x in range(0, size):
        AtchVar = Placement + (OptVar * x)
        Attach.append(AtchVar)
    return Attach

#%%
# Checks for the area that a ship is being placed if it is empty or contains a ship
#######################################################################  
# Function:   ClearSeas
# Description:  forces there not to be multiple ships in the same location
# Parameters:   all other functions working and a board to check loactions against
# Return values:  True or False
# Pre-Conditions:  board state and turn plus locations to test 
# Post-Conditions:   variable to store true or false
####################################################################### 
def ClearSeas(Attach, whosTurn):
    OpenSea = True
    if whosTurn == "Player":
        for x in range(0, len(Attach)):
            if Player[Attach[x]] == 0:
                pass
            else:
                OpenSea = False
    if whosTurn == "AI":
        for x in range(0, len(Attach)):
            if AI[Attach[x]] == 0:
                pass
            else:
                OpenSea = False
    return OpenSea



#%%
# 5 Carrier 6 battleship 7 cruiser 8 submarine 9 destroyer
# If the ship placement locations are valid enters them into the grid or boards
#######################################################################  
# Function:   Admiral
# Description:  Makes your ships set sail or just places them on the board
# Parameters:   ships the attach function and whos turn it is
# Return values:  an updated board
# Pre-Conditions:  all inputs work
# Post-Conditions:   board is updated 
####################################################################### 
def Admiral(Attach, ship, whosTurn):
    if whosTurn == "Player":
        for x in range(0, len(Attach)):
            Player[Attach[x]] = ship
    if whosTurn == "AI":
        for x in range(0, len(Attach)):
            AI[Attach[x]] = ship
    return

#%%
# makes me not have to type out the ship names 10000 times
#######################################################################  
# Function:   shipNames
# Description:  Makes using ship names much easier *was created after the attack function
# Parameters:   an input number
# Return values:  string with the ship na e
# Pre-Conditions:  valid inputs
# Post-Conditions:   an output variable
####################################################################### 
def shipNames(shipDex):
    if shipDex == 5:
        shipName = "Carrier"
    elif shipDex == 6:
        shipName = "Battleship"
    elif shipDex == 7:
        shipName = "Cruiser"
    elif shipDex == 8:
        shipName = "Submarine"
    elif shipDex == 9:
        shipName = "Destroyer"
    return shipName


#%%
# Places ships for the player and AI
#######################################################################  
# Function:   PlaceShips
# Description:  Runs all of the functions required to have ship placement
# Parameters:   ALL the other functions and the user inputs and AI random inputs
# Return values:  a properly set up board for both the player and AI
# Pre-Conditions:  A lot of stuff like boards existing and the other functions all working
# Post-Conditions:   everything is put into the proper board condition
####################################################################### 
def PlaceShips(whosTurn):
    shipLDic = {5:5, 6:4, 7:3, 8:3, 9:2}
    if whosTurn == "Player":
        for x in range(5, 10):
            while True:
                print(MsgPl, shipNames(x))
                Size = shipLDic[x]
                Plcmt = position()
                optCh = optlist(Plcmt, Size)
                Attached = shipCheck(Plcmt, Size, optCh)
                if ClearSeas(Attached, whosTurn) == True:
                    break
            Admiral(Attached, x, whosTurn)
    elif whosTurn == "AI":
        print("AI places ships.")
        for x in range(5, 10):
            while True:
                Size = shipLDic[x]
                Plcmt = int(rng.integers(low = 0, high = 100, size = 1))
                optCh = AIoptlist(Plcmt, Size)
                Attached = shipCheck(Plcmt, Size, optCh)
                if ClearSeas(Attached, whosTurn) == True:
                    break
            Admiral(Attached, x, whosTurn)
    return




#%%
# Convert position to grid/board location 
#######################################################################  
# Function:   backwardsconvert
# Description:  changes positions on the board back into typical battleship coordinates
# Parameters:   position on a board
# Return values:  the converted back string
# Pre-Conditions:  
# Post-Conditions:   
####################################################################### 

letDic = {0:"A", 10:"B", 20:"C", 30:"D", 40:"E", 50:"F", 60:"G", 70:"H", 80:"I", 90:"J",}
def backwardsconvert(posit):
    numeral = (posit // 10) * 10
    letter = letDic[numeral]
    numbnum = (posit - numeral) + 1
    backCon = letter + str(numbnum)
    return backCon


#%%
#Creates the grids or the 'boards' for playing on
#######################################################################  
# Function:   creategrid
# Description:  creates the blank boards to play on
# Parameters:   none
# Return values:  a board
# Pre-Conditions:  
# Post-Conditions:   
####################################################################### 

def creategrid():
    a = {}
    k = 0
    while k < 100:
        # dynamically create key
        key = k
        # calculate value
        value = 0
        a[key] = value 
        k += 1
    return a

#%%
#creates turn actions
#1s are hits
#0 are empties
#2 are misses
#5 is carrier with size 5
#6 is battleship with size 4
#7 is crusier with size 3
#8 is submarine with size 3
#9 is destroyer with size 2
# 100 total space with 17 occupied spaces
# function which determines the hits and misses and what was hit
#######################################################################  
# Function:   attack
# Description:  allows ai and player to attack places on boards
# Parameters:   the inputs of player
# Return values:  hits misses already attacked there or invalid inpu
# Pre-Conditions:  the game has been set up and boards placed
# Post-Conditions:   something to accept the values I guess
####################################################################### 
def attack(whosTurn):
    if whosTurn == "Player":
        print("Your turn. Choose a position to attack:")
        x = 0
        while x == 0:
            pos = position()
            if AI[pos] == 5:
                AI[pos] = 1
                print("Hit, Carrier")
                x = 1
            elif AI[pos] == 6:
                AI[pos] = 1
                print("Hit, Battleship")
                x = 1
            elif AI[pos] == 7:
                AI[pos] = 1
                print("Hit, Crusier")
                x = 1
            elif AI[pos] == 8:
                AI[pos] = 1
                print("Hit, Submarine")
                x = 1
            elif AI[pos] == 9:
                AI[pos] = 1
                print("Hit, Destroyer")
                x = 1
            elif AI[pos] == 2:
                print("You already attacked that position. Please attack again.")
            else:
                print("Miss")
                AI[pos] = 2
                x = 1
    elif whosTurn == "AI":
        x = 0
        while x == 0:
            pos = int(rng.integers(low = 0, high = 100, size = 1))
            if Player[pos] == 5:
                Player[pos] = 1
                print("Your carrier was hit at ", backwardsconvert(pos))
                x = 1
            elif Player[pos] == 6:
                Player[pos] = 1
                print("Your battleship was hit at ", backwardsconvert(pos))
                x = 1
            elif Player[pos] == 7:
                Player[pos] = 1
                print("Your crusier was hit at ", backwardsconvert(pos))
                x = 1
            elif Player[pos] == 8:
                Player[pos] = 1
                print("Your submarine was hit at ", backwardsconvert(pos))
                x = 1
            elif Player[pos] == 9:
                Player[pos] = 1
                print("Your destroyer was hit at ", backwardsconvert(pos))
                x = 1
            elif Player[pos] == 2:
                pass
            else:
                print("Enemy missed at ", backwardsconvert(pos))
                Player[pos] = 2
                x = 1
    return 

#%%
# Creates boards for both player and AI
Player = creategrid()
#print(Player)
AI = creategrid()
#print(AI)

#%%
#test for the attack function
"""
AI[5] = 5
AI[15] = 5
AI[25] = 5
AI[35] = 5
AI[45] = 5

attack("Player")
"""
#%% image testing area. Stretch goal
"""
from PIL import Image
Wid = 400
Hei = 400

img  = Image.new(mode = "RGB", size = (Wid, Hei))
img.show()
"""

#%%
#   I T S   G A M E   D A Y


#Places ships before the game for the player and the AI
PlaceShips("Player")
PlaceShips("AI")


print("Player board")
print(Player)

#DELETE THE PRINT AI OR THIS GAME WILL SUCK
#print("AI board")
#print(AI)


#PLAYS THE GAME
Turn = "Player"
while True:
    attack(Turn)
    if Turn == "Player":
        Turn = "AI"
    elif Turn == "AI":
        Turn = "Player"
    AIScore = scoreFuncAI()
    PlayerScore = scoreFuncP()
    if AIScore == 17:
        break
    elif PlayerScore == 17:
        break
    else:
        pass

#used to declare winner
PlayerFS = scoreFuncAI()
AIFS = scoreFuncP()

# Shows who won the game
if PlayerFS == 17:
    print("Player wins. Thank you for playing.")
elif AIFS == 17:
    print("AI wins. Thank you for playing.")
    
#%% Show board state
examp = 3

firsts = [1, 21, 31, 41, 51, 61, 71, 81, 91]
seconds = [2, 22, 32, 42, 52, 62, 72, 82, 92]
thirds = [3, 23, 33, 43, 53, 63, 73, 83, 93]

def BoardShow(AIB, PlayB):
    if examp in firsts:
        ordSuf = "st"
    elif examp in seconds:
        ordSuf = "nd"
    elif examp in thirds:
        ordSuf = "rd"
    else:
        ordSuf = "th"
    print(f"It is the end of the {examp}{ordSuf} turn.\n")
    print("Would you like to see board states?")
    while True:
        x = input("0 for no, 1 for your board, 2 for enemy board (current hits misses and empty spaces), \n 3 for both 1 and 2\n")
        print(x)
        if x == (0 or 1 or 2 or 3):
            break
    if x == 0:
        pass
    elif x == 1:
        pass
    return

BoardShow(0,0)


#%% Player board state

def ShowGridP(Player):
    
    return

#%% I don't understand I think im rarded
x = 0
while True:
    x = x + 1
    print(x)
    if x == (0 or 5):
        break









