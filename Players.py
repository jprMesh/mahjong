class Player:
    """Mahjong player class"""

    def __init__(self, wind, wall):
        self.wind = wind
        self.hand = []
        self.faceup = []
        self.loadHand(wall)

    # Load a starting hand from the game wall
    def loadHand(self, wall):
        for i in range(13):
            self.hand.append(wall.pop())

    # Draw from the wall
    def draw(self, wall):
        self.hand.append(wall.pop())

    # Put tiles face up
    def putFaceUp(self, tile):
        self.faceup.append(tile)
        self.hand.remove(tile)

    # Discard a tile (pass in copy of tile you want to discard)
    def discard(self, tile, game):
        game.pile.append(tile)
        self.hand.remove(tile)
        game.turnIndic = (self.wind + 1) % 4

    def handContains(self, digit):
        for tile in self.hand:
            if tile.value == digit:
                return True
        return False
