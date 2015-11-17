from Tile import Tile
from Players import Players
from random import randint
from random import shuffle
from random import choice

#Dice rolling function
#3 dice are rolled instead of one 18 sided die
#This probably makes dice graphics easier later
def diceRoll():
    dice1 = Random.randint(1,6)
    dice2 = Random.randint(1,6)
    dice3 = Random.randint(1,6)
    totalSum = dice1 + dice2 + dice3
    return totalSum

suits = ["Bamboo", "Dot", "Character", "Honor"]
winds = ["East", "South", "West", "North"]
honorValues = ["E", "S", "W", "N", "R", "G", "B", "Flower", "Season"]

class Mahjong():
    """Game management class"""
    def __init__(self):
        self.generateWall()
        #self.addPlayers()
        self.prevailingWind = choice(winds)

    def generateWall(self):
        self.wall = [Tile(suit, val+1+(suit=="Honor")*10)
                for suit in suits
                for val in xrange(9)
                for x in xrange(4)]
        shuffle(self.wall)

    def addPlayers(self):
        self.players = [Players(wind) for wind in winds]

Mahjong()
