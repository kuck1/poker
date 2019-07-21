from cards import Deck
from hand import Hand
from hand import Card

def high_card():
	cards = [Card() for i in xrange(3)]

	cards[0].value = 10
	cards[1].value = 9
	cards[2].value = 2

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10:
		print("High card fail")
		print(h.strength)
	else:
		print("High card pass")

def one_pair():
	cards = [Card() for i in xrange(3)]

	cards[0].value = 10
	cards[1].value = 10
	cards[2].value = 2

	h = Hand(cards)
	h.update_strength()

	if h.strength != 1002:
		print("One pair fail")
		print(h.strength)
	else:
		print("One pair pass")

def two_pair():
	cards = [Card() for i in xrange(5)]

	cards[0].value = 10
	cards[1].value = 10
	cards[2].value = 9
	cards[3].value = 9
	cards[4].value = 2

	cards[0].suit = 1
	cards[1].suit = 2
	cards[2].suit = 3
	cards[3].suit = 2
	cards[4].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 100902:
		print("Two pair fail")
		print(h.strength)
	else:
		print("Two pair pass")

def three_of_a_kind():
	cards = [Card() for i in xrange(3)]

	cards[0].value = 10
	cards[1].value = 10
	cards[2].value = 10

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 7:
		print("Three of a kind fail")
		print(h.strength)
	else:
		print("Three of a kind pass")

def straight():
	cards = [Card() for i in xrange(5)]

	cards[0].value = 6
	cards[1].value = 7
	cards[2].value = 8
	cards[3].value = 9
	cards[4].value = 10

	cards[0].suit = 1
	cards[1].suit = 2
	cards[2].suit = 3
	cards[3].suit = 4
	cards[4].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 9:
		print("Straight fail")
		print(h.straight)
		print(h.strength)
	else:
		print("Straight pass")

def flush():
	cards = [Card() for i in xrange(5)]

	cards[0].value = 2
	cards[1].value = 3
	cards[2].value = 4
	cards[3].value = 6
	cards[4].value = 10

	cards[0].suit = 1
	cards[1].suit = 1
	cards[2].suit = 1
	cards[3].suit = 1
	cards[4].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 11:
		print("Flush fail")
		print(h.strength)
	else:
		print("Flush pass")

def full_house():
	cards = [Card() for i in xrange(5)]

	cards[0].value = 9
	cards[1].value = 9
	cards[2].value = 10
	cards[3].value = 10
	cards[4].value = 10

	cards[0].suit = 1
	cards[1].suit = 1
	cards[2].suit = 1
	cards[3].suit = 1
	cards[4].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 13 + 10 ** 10 * 9:
		print("Full House fail")
		print(h.strength)
	else:
		print("Full House pass")

def four_of_a_kind():
	cards = [Card() for i in xrange(5)]

	cards[0].value = 9
	cards[1].value = 10
	cards[2].value = 10
	cards[3].value = 10
	cards[4].value = 10

	cards[0].suit = 1
	cards[1].suit = 1
	cards[2].suit = 1
	cards[3].suit = 1
	cards[4].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 15:
		print("Four of a kind fail")
		print(h.strength)
	else:
		print("Four of a kind pass")

def straight_flush():
	cards = [Card() for i in xrange(6)]

	cards[0].value = 6
	cards[1].value = 7
	cards[2].value = 8
	cards[3].value = 9
	cards[4].value = 10
	cards[5].value = 11

	cards[0].suit = 2
	cards[1].suit = 2
	cards[2].suit = 2
	cards[3].suit = 2
	cards[4].suit = 2
	cards[5].suit = 1

	h = Hand(cards)
	h.update_strength()

	if h.strength != 10 ** 17:
		print("Straight Flush fail")
		print(h.strength)
	else:
		print("Straight Flush pass")

high_card()
one_pair()
two_pair()
three_of_a_kind()
straight()
flush()
full_house()
four_of_a_kind()
straight_flush()




