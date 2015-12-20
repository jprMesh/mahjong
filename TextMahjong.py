from Mahjong import Mahjong

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    gg = Mahjong()
    print("Welcome to HK Mahjong.\nThe prevailing wind is currently "+
          Mahjong.winds[gg.prevailingWind]+
          ". The move is to the "+Mahjong.winds[gg.turnIndic]+" player.")
    while 1:

        # Draw phase
        print("\n"+Mahjong.winds[gg.turnIndic]+", this is your hand:")
        for item in gg.players[gg.turnIndic].hand:
            print(item)
        if gg.pile:
            print("The top of the discard pile is: "+str(gg.pile[-1]))
        else:
            print("There is no discard pile.")
        while 1:
            drawfrom = input("From where would you like to draw?\n> ")
            if drawfrom.lower() == "wall":
                gg.players[gg.turnIndic].draw(gg.wall)
                break
            elif drawfrom.lower() == "pile" and gg.pile:
                gg.players[gg.turnIndic].draw(gg.pile)
                break
            else:
                print("Invalid draw location")

        # Do some sort of win condition checking here?

        # Discard phase
        print("Your hand is now:")
        for tilenum in range(len(gg.players[gg.turnIndic].hand)):
            print(str(tilenum).rjust(2)+"  "+str(gg.players[gg.turnIndic].hand[tilenum]))
        while 1:
            discardID = input("Which tile would you like to discard?\n> ")
            if isInt(discardID) and int(discardID) < len(gg.players[gg.turnIndic].hand):
                gg.players[gg.turnIndic].discard(gg.players[gg.turnIndic].hand[int(discardID)], gg)
                break
