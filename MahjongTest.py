import unittest
import random
from Tile import Tile
from Mahjong import Mahjong

class MahjongTest(unittest.TestCase):

    def setUp(self):
        self.mjgame = Mahjong()

    def tearDown(self):
        del self.mjgame

    def testPlayers(self):
        self.assertEqual(len(self.mjgame.players), 4)
        self.assertEqual(self.mjgame.prevailingWind, "East")

    def testWall(self):
        self.assertEqual(len(self.mjgame.wall), (4*4*9)-(13*4))

    def testHand(self):
        self.assertEqual(len(self.mjgame.players[0].hand), 13)

    def testHandContains(self):
        for x in range(13):
            self.mjgame.players[0].hand.pop()
        randvalue = random.randint(1,9)
        randtile = Tile(random.choice(["Bamboo", "Dot", "Character", "Honor"]), randvalue)
        self.mjgame.players[0].hand.append(randtile)
        self.assertTrue(self.mjgame.players[0].handContains(randvalue))
        self.mjgame.players[0].hand.pop()
        self.assertFalse(self.mjgame.players[0].handContains(randvalue))

if __name__ == '__main__':
    unittest.main()