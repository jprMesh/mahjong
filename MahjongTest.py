import unittest
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
        self.assertEqual(len(self.mjgame.wall), 4*4*9-(13*4))

    def testHand(self):
        self.assertEqual(len(self.mjgame.players[0].hand), 13)

if __name__ == '__main__':
    unittest.main()