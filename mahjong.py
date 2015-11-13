from mahjong import Tile

suits = ["Bamboo", "Dot", "Character", "Honor"]
honorValues = ["E", "S", "W", "N", "R", "G", "B", "Flower", "Season"]
wall = []   #initialize empty wall list

for i in range(0,3):    #4 copies of every tile
    for suit in suits[0:3]:     #for suited tiles
        for n in range(1,10):   #numbers 1-9
            tile = Tile(suit=suit, value=n)
            wall.append(tile)
    for value in honorValues:   #for honor tiles
        tile = Tile(suit="Honor", value=value)
        wall.append(tile)
