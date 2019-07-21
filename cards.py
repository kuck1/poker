import random


class Card:
	suit = 0
	value = 0


class Deck:
	cards = [Card() for i in xrange(52)]

	def __init__(self):
		suits = [1,2,3,4]
		values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		card_idx = 0

		for card in self.cards:
			suit_idx = card_idx / 13
			value_idx = card_idx / 4

			card.suit = suits[suit_idx]
			card.value = values[value_idx]
			card_idx += 1

		self.shuffle()

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_card(self):
		card = self.cards.pop(0)
		return card;

