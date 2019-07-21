from cards import Card
from itertools import compress

class Hand:
	cards = []
	strength = 0
	
	straight_flush = 0
	sf_straight = 0
	sf_flush = 0 
	four_of_a_kind = 0
	flush = 0
	straight = 0
	three_of_a_kind = 0
	high_pair = 0
	low_pair = 0
	high_card = 0
	kicker = 0

	def __init__(self, cards):
		self.cards = cards


	def update_strength(self):
		self.check_for_flush()
		self.check_for_straight()
		self.check_for_straight_flush()
		self.check_for_dupes()

		self.calc_strength()

	def calc_strength(self):
		if self.straight_flush:
			self.strength = self.straight_flush * 10 ** 16
		elif self.four_of_a_kind:
			self.strength = self.four_of_a_kind * 10 ** 14
		elif self.three_of_a_kind and self.high_pair:
			self.strength = self.three_of_a_kind * 10 ** 12 + self.high_pair * 10 ** 10
		elif self.flush:
			self.strength = self.flush * 10 ** 10
		elif self.straight:
			self.strength = self.straight * 10 ** 8
		elif self.three_of_a_kind:
			self.strength = self.three_of_a_kind * 10 ** 6 + self.kicker
		elif self.low_pair:
			self.strength = self.high_pair * (10 ** 4) + self.low_pair * (10 ** 2) + self.kicker
		elif self.high_pair:
			self.strength = self.high_pair * 10 ** 2 + self.kicker
		else:
			self.strength = self.high_card

	def check_for_straight_flush(self):
		while(1):
			if self.sf_straight == self.sf_flush:
				self.straight_flush = self.sf_straight
				return

			elif self.sf_straight == 0 or self.sf_flush == 0 or not self.sf_straight or not self.sf_flush:
				return

			elif self.sf_straight > self.sf_flush:
				self.remove_card(self.sf_straight)

			else:
				self.remove_card(self.sf_flush)

			self.check_for_flush()
			self.check_for_straight()

	def remove_card(self, remove_value):
		cards = [card for card in self.cards if card.value != remove_value]
		self.cards = cards

	def check_for_flush(self):
		suits = self.get_suits()

		dupes = [x for n, x in enumerate(suits) if x in suits[:n]]

		dupes = self.unique(dupes)

		for dupe in dupes:
			if suits.count(dupe) >= 5:
				high_value = self.get_flush_high_value(dupe)
				self.sf_flush = high_value
				if self.flush == 0:
					self.flush = high_value

	def get_flush_high_value(self, flush_suit):
		flush_cards_idx = [card.suit == flush_suit for card in self.cards]
		flush_cards = compress(self.cards, flush_cards_idx)
		high_value = 0
		for card in flush_cards:
			if card.value > high_value:
				high_value = card.value
		return high_value

	def check_for_straight(self):
		values = self.get_values()
		values.sort()
		straight = 0
		if values and len(values) >= 5:
			for i in xrange(len(values)-4):
				straight = self.check_span(values, i)

		self.sf_straight = straight
		if self.straight == 0:
			self.straight = straight

	def check_span(self, values, start):
		span = values[start + 4] - values[start]
		if span == 4:
			return values[start + 4]

	def check_for_dupes(self):

		values = self.get_values()

		dupes = [x for n, x in enumerate(values) if x in values[:n]]

		dupes = self.unique(dupes)

		if self.is_four_of_a_kind(dupes, values):
			return

		dupes = self.check_three_of_a_kind(dupes, values)

		self.set_pairs_or_high_card(dupes, values)
		

	def is_four_of_a_kind(self, dupes, values):
		for dupe in dupes:
			count = values.count(dupe)
			if count == 4:
				self.four_of_a_kind = dupe
				return True

		return False

	def check_three_of_a_kind(self, dupes, values):
		dupes.sort(reverse=True)

		for dupe in dupes:
			count = values.count(dupe)
			if count == 3:
				self.three_of_a_kind = dupe
				dupes.remove(dupe)

				return dupes


		return dupes

	def set_pairs_or_high_card(self, dupes, values):
		if not dupes:
			self.high_card = values[0]
			return

		self.high_pair = dupes[0]

		if len(dupes) == 1:
			self.set_kicker(dupes, values, 1)
		else:
			self.low_pair = dupes[1]
			self.set_kicker(dupes, values, 2)
	

	def set_kicker(self, dupes, values, pairs):
		for i in xrange(pairs):
			values = [x for x in values if x != dupes[i]]

		if values:
			self.kicker = values[0]

	def get_values(self):
		values = []
		for card in self.cards:
			values.append(card.value)

		values.sort(reverse=True)
		
		return values

	def get_suits(self):
		suits = []

		for card in self.cards:
			suits.append(card.suit)

		suits.sort(reverse=True)
		
		return suits

	def unique(self, list1): 
	    list_set = set(list1) 
	    unique_list = (list(list_set))
	    return unique_list

