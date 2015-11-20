from Tile import Tile
from Players import Player
import random

class Mahjong:
    """Game management class"""

    # Static Variables
    suits = ["Bamboo", "Dot", "Character", "Honor"]
    winds = ["East", "South", "West", "North"]
    honor_values = ["E", "S", "W", "N", "R", "G", "B", "Flower", "Season"]

    @staticmethod
    def roll3d6():
        dice1 = Random.randint(1,6)
        dice2 = Random.randint(1,6)
        dice3 = Random.randint(1,6)
        totalSum = dice1 + dice2 + dice3
        return totalSum

    def __init__(self):
        self.generateWall()
        self.addPlayers()
        self.prevailingWind = "East"

    def generateWall(self):
        self.wall = [Tile(suit, val+1+(suit=="Honor")*10)
                for suit in Mahjong.suits
                for val in xrange(9)
                for x in xrange(4)]
        random.shuffle(self.wall)

    def addPlayers(self):
        self.players = [Player(wind, self.wall) for wind in Mahjong.winds]

game = Mahjong()
print game.players[0].hand
