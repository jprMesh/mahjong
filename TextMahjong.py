from Mahjong import Mahjong

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def printHand(gg):
    print(Mahjong.winds[gg.turnIndic]+", your hand is now:")
    for tilenum in range(len(gg.players[gg.turnIndic].hand)):
        print(chr(tilenum+97)+"  "+str(gg.players[gg.turnIndic].hand[tilenum]))

def drawphase(gg):
    printHand(gg)
    if gg.pile:
        print("The top of the discard pile is: "+str(gg.pile[-1]))
    else:
        print("There is no discard pile.")
    drawfrom = input("From where would you like to draw?\n> ")
    if drawfrom.lower() == "wall":
        gg.players[gg.turnIndic].draw(gg.wall)
    elif drawfrom.lower() == "pile" and gg.pile:
        gg.players[gg.turnIndic].draw(gg.pile)
    else:
        print("Invalid draw location")
        return
    gg.phase = "discard"

def discardphase(gg):
    printHand(gg)
    discardIndex = input("Which tile would you like to discard?\n> ")
    if discardIndex[0].lower() and ord(discardIndex[0])-97 < len(gg.players[gg.turnIndic].hand):
        gg.players[gg.turnIndic].discard(gg.players[gg.turnIndic].hand[ord(discardIndex[0])-97], gg)
        print(Mahjong.winds[(gg.turnIndic-1)%4]+" discarded "+str(gg.pile[-1])+".")
        gg.phase = "pungchi"

def pungchiphase(gg):
    pungs = input("Players calling pung?\n> ")
    if pungs:
        for x in range(3):
            nextplayer = (gg.turnIndic+1+x)%4
            if str(nextplayer) in pungs:
                gg.players[nextplayer].draw(gg.pile)
                gg.turnIndic = nextplayer
                gg.phase = "flipup"
                return
    chis = input("Players calling chi?\n> ")
    if chis:
        for x in range(3):
            nextplayer = (gg.turnIndic+1+x)%4
            if str(nextplayer) in chis:
                gg.players[nextplayer].draw(gg.pile)
                gg.turnIndic = nextplayer
                gg.phase = "flipup"
                return
    gg.phase = "draw"

def flipupphase(gg):
    printHand(gg)
    gg.players[gg.turnIndic].putFaceUp(gg.players[gg.turnIndic].hand[-1])
    while 1:
        fliptiles = input("Which other tiles would you like to flip up?\n> ")
        if len(fliptiles) is 2:
            for x in fliptiles:
                if x.lower() and ord(x)-97 < len(gg.players[gg.turnIndic].hand):
                    gg.players[gg.turnIndic].putFaceUp(gg.players[gg.turnIndic].hand[ord(x)-97])
            break
    gg.phase = "discard"

if __name__ == '__main__':
    mgame = Mahjong()
    print("Welcome to HK Mahjong.\nThe prevailing wind is currently "+
          Mahjong.winds[mgame.prevailingWind]+
          ". The move is to the "+Mahjong.winds[mgame.turnIndic]+" player.")
    
    while 1:
        if mgame.phase is "draw":
            drawphase(mgame)
        # Do some sort of win condition checking here?
        elif mgame.phase is "discard":
            discardphase(mgame)
        elif mgame.phase is "pungchi":
            pungchiphase(mgame)
        elif mgame.phase is "flipup":
            flipupphase(mgame)