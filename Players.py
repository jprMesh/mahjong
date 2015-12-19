class Player:
    """Mahjong player class"""

    def __init__(self, wind, wall):
        self.wind = wind
        self.hand = []
        self.loadHand(wall)

    def loadHand(self, wall):
        for i in range(13):
            self.hand.append(wall.pop())

    #draw from the wall, normal animation
    def draw(self, wall):
        self.hand.append(wall.pop())

    #draw from the wall, but have the animation draw from the back
    def backDraw(self):
        self.hand.append(wall.pop())

    #discard a tile, need to choose by mouse movements
    def discard(self, tile, game):
        game.pile = tile
        self.hand.remove(tile)
        game.turnIndic = (game.turnIndic + 1) % 4

    def handContains(self, digit):
        for tile in self.hand:
            if tile.value == digit:
                return True
        return False
