import random

class Card:
    # Constructor

    def __init__(self, value):
        # self.value goes from 2 to 14
        # 2 is two
        # 10 is ten
        # 11 is jack
        # 13 is king
        # 14 is ace
        self.value = value

    def conpareTo(otherCard):
        # returns negative number if the other card is bigger
        # returns positive number if this card is bigger
        # reurns 0 if they are the same
        return this.value - otherCard.value


class Deck:
    # Constructor
    def __init__(self):
        self.cardList = []
        for cardValues in range(2,15):
            for makeFourCards in range(4):
                self.cardList.append(Card(cardValues))
    def print(self):
        for card in self.cardList:
            print(str(card.value))
    def shuffle(self):
        random.shuffle(self.cardList)

deck = Deck()
deck.shuffle()
deck.print()

class Player:
    def __init__(self, hand):

