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

    def compareTo(self, otherCard):
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
    def deal(self, amount, playerone, playertwo):
        for i in range(amount):
            playerone.recieve(self.cardList.pop())
            playerone.recieve(self.cardList.pop())

deck = Deck()
deck.shuffle()
deck.print()

class Player:
    def __init__(self, hand):
        self.hand = hand
    def give(self, player):
        player.recieve(self.hand.pop())
    def recieve(self, cards):
        self.hand.append(cards)