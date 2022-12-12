import random


class Card:
    def __init__(self,value,suit):
        self.value=value
        #diamonds, clubs, hearts, spades
        self.suit=suit

    def print_info(self):
        print(f'{self.value} of {self.suit}')


class Deck:
    def __init__(self,cards):
        self.cards=cards

    def add_card(self,card):
        self.cards.append(card)

    def random_pick(self):
        randCard=random.choice(self.cards)
        return randCard.print_info()

    def shuffle(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for card in deck.cards:
            card.print_info()


card1=Card('5','diamonds')
card2=Card('10','hearts')
card3=Card('Q','spades')
card4=Card(2,'clubs')
card5=Card(5,'hearts')

print('card info:')
card1.print_info()
cards=[card1,card2,card3,card4,card5]


deck=Deck(cards)

print('random pick:')
deck.random_pick()
print('deck:')
deck.print_deck()
print('shuffle')
deck.shuffle()
print('shuffled')
deck.print_deck()



