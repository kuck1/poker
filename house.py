


class Dealer:
	deck = []

	__init__(self):
		pass

	def shuffle(self):
		deck = Deck()

	def deal_hands(self, players):
		deck = Deck()

		hands = [TexasHand() for i in xrange(players)]

		for card in xrange(2):
			for hand in xrange(players): 
				hands[hand_idx][card_idx] = deck.deal_card()

		return hands

class TexasHand:
	cards = [Cards() for i in xrange(2)]