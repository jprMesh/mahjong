from Mahjong import Mahjong

class TextMahjong(Mahjong):
    """Command line implementation of Mahjong"""
    
    # Print the current player's hand
    def printHand(self):
        print(Mahjong.winds[self.turnIndic]+", your hand is now:")
        for tilenum in range(len(self.players[self.turnIndic].hand)):
            print(chr(tilenum+97)+"  "+str(self.players[self.turnIndic].hand[tilenum]))

    def drawPhase(self):
        self.printHand()
        if self.pile:
            print("The top of the discard pile is: "+str(self.pile[-1]))
        else:
            print("There is no discard pile.")
        drawfrom = input("From where would you like to draw?\n> ")
        if drawfrom.lower() == "wall":
            self.players[self.turnIndic].draw(self.wall)
        elif drawfrom.lower() == "pile" and self.pile:
            self.players[self.turnIndic].draw(self.pile)
        else:
            print("Invalid draw location")
            return
        self.phase = "discard"

    def discardPhase(self):
        self.printHand()
        discardIndex = input("Which tile would you like to discard?\n> ")
        if discardIndex[0].lower() and ord(discardIndex[0])-97 < len(self.players[self.turnIndic].hand):
            self.players[self.turnIndic].discard(self.players[self.turnIndic].hand[ord(discardIndex[0])-97], self)
            print(Mahjong.winds[(self.turnIndic-1)%4]+" discarded "+str(self.pile[-1])+".")
            self.phase = "pung"

    def pungPhase(self):
        pungs = input("Players calling pung?\n> ")
        if pungs:
            for x in range(3):
                nextplayer = (self.turnIndic+1+x)%4
                if str(nextplayer) in pungs:
                    self.players[nextplayer].draw(self.pile)
                    self.turnIndic = nextplayer
                    self.phase = "faceup"
                    return
        self.phase = "chi"

    def chiPhase(self):
        chis = input("Players calling chi?\n> ")
        if chis:
            for x in range(3):
                nextplayer = (self.turnIndic+1+x)%4
                if str(nextplayer) in chis:
                    self.players[nextplayer].draw(self.pile)
                    self.turnIndic = nextplayer
                    self.phase = "faceup"
                    return
        self.phase = "draw"

    def faceupPhase(self):
        self.printHand()
        self.players[self.turnIndic].putFaceUp(self.players[self.turnIndic].hand[-1])
        while 1:
            fliptiles = input("Which other tiles would you like to flip up?\n> ")
            if len(fliptiles) is 2:
                for x in fliptiles:
                    if x.lower() and ord(x)-97 < len(self.players[self.turnIndic].hand):
                        self.players[self.turnIndic].putFaceUp(self.players[self.turnIndic].hand[ord(x)-97])
                break
        self.phase = "discard"

    def playGame(self):
        print("Welcome to HK Mahjong.\nThe prevailing wind is currently "+
              Mahjong.winds[self.prevailingWind]+
              ". The move is to the "+Mahjong.winds[self.turnIndic]+" player.")
        while 1:
            if self.phase is "draw":
                self.drawPhase()
            # Do some sort of win condition checking here?
            elif self.phase is "discard":
                self.discardPhase()
            elif self.phase is "pung":
                self.pungPhase()
            elif self.phase is "chi":
                self.chiPhase()
            elif self.phase is "faceup":
                self.faceupPhase()

if __name__ == '__main__':
    tgame = TextMahjong()
    tgame.playGame()
