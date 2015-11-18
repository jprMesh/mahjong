class Players:
    """Mahjong player class"""

    def __init__(self, wind, wall):
        self.wind = wind
        self.hand = []
        self.loadHand(wall)

    def loadHand(self, wall):
        for i in xrange(13):
            self.hand.append(wall.pop())

    #draw from the wall, normal animation
    def draw():
        hand.append(wall.pop())

    #draw from the wall, but have the animation draw from the back
    def backDraw():
        hand.append(wall.pop())

    #discard a tile, need to choose by mouse movements
    def discard(tile):
        hand.pop(tile)