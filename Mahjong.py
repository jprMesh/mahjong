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
        self.prevailingWind = 0
        self.pile = []
        self.turnIndic = 0
        self.phase = "draw"

    def generateWall(self):
        self.wall = [Tile(suit, val+1+(suit=="Honor")*10)
                     for suit in Mahjong.suits
                     for val in range(9)
                     for x in range(4)]
        random.shuffle(self.wall)

    def addPlayers(self):
        self.players = [Player(index, self.wall) for index in range(4)]

    # Maybe these should have default implementations
    # def drawPhase(self):
    #     something

    # def discardPhase(self):
    #     something

    # def pungPhase(self):
    #     something

    # def chiPhase(self):
    #     something

    # def faceupPhase(self):
    #     something
