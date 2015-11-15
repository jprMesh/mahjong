from Tile import Tile
from Players import Players
from random import randint
from random import shuffle

#Dice rolling function
#3 dice are rolled instead of one 18 sided die
#This probably makes dice graphics easier later
def diceRoll():
    dice1 = Random.randint(1,6)
    dice2 = Random.randint(1,6)
    dice3 = Random.randint(1,6)
    totalSum = dice1 + dice2 + dice3
    return totalSum

#set up the game
def loadHand():
    for i in range(13)
        hand.append(wall.pop())

suits = ["Bamboo", "Dot", "Character", "Honor"]
honorValues = ["E", "S", "W", "N", "R", "G", "B", "Flower", "Season"]
winds = ["East", "South", "West", "North"]
wall = []   #initialize empty wall list
hand = []
diceRolls = []
prevailingWind = "" 

#Populate the tiles list
for i in range(4):    #4 copies of every tile
    for suit in suits[:3]:     #for suited tiles
        for n in range(10):   #numbers 1-9
            tile = Tile(suit=suit, value=n)
            wall.append(tile)
    for value in honorValues:   #for honor tiles
        tile = Tile(suit="Honor", value=value)
        wall.append(tile)
shuffle(wall)

#set up the Players
loadHand()
player1 = Player(hand=hand)
hand[:] = []
loadHand()
player2 = Player(hand=hand)
hand[:] = []
loadHand()
player3 = Player(hand=hand)
hand[:] = []
loadHand()
player4 = Player(hand=hand)
diceRolls.append(diceRoll())
diceRolls.append(diceRoll())
diceRolls.append(diceRoll())
diceRolls.append(diceRoll())
for i in range(4)
