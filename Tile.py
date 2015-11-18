class Tile:
    """Mahjong tile class"""

    def __init__(self, suit, value):   
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Tile: <" + self.suit + " " + str(self.value) + ">"

    def __str__(self):
        return "<" + self.suit + " " + str(self.value) + ">"