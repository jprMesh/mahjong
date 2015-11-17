class Tile:
    suit = ""   #dot, bamboo, character, honor
    value = ""  #1-9, R, G, B, E, S, W, N, flower, season
    def __init__(self, suit, value):   
        self.suit = suit
        self.value = value
    def __eq__(self, other):
    	return self.__dict__ == other.__dict__
