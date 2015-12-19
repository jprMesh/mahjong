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
        self.assertTrue(self.mjgame.players[0].handContains(self.mjgame.players[0].hand[5].value))
        self.assertFalse(self.mjgame.players[0].handContains(20))

    def testDiscard(self):
        length = len(self.mjgame.players[1].hand)
        tile = self.mjgame.players[1].hand[3]
        self.mjgame.players[1].discard(tile, self.mjgame)
        self.assertEqual(len(self.mjgame.players[1].hand), length-1)
        self.assertEqual(self.mjgame.pile, tile)

    def testDraw(self):
        handlen = len(self.mjgame.players[2].hand)
        walllen = len(self.mjgame.wall)
        self.mjgame.players[2].draw(self.mjgame.wall)
        self.assertEqual(len(self.mjgame.players[2].hand), handlen+1)
        self.assertEqual(len(self.mjgame.wall), walllen-1)

if __name__ == '__main__':
    unittest.main()