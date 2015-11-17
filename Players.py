class Players:
    wind = ""   #E, S, W, N
    hand = []   #initialize empty hand list
    displayedTiles = []

    def __init__(self, wind):
        self.wind = wind
        self.loadHand()

    def loadHand(self):
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

    #Win conditions
    #def winConditionCheck(hand):
