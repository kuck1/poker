from cards import Deck


class Game:
	players = [];
	player_data = []

	dealer = Dealer()

	def __init__(self):
		players[0] = ai1()
		players[1] = ai2()

		player_data = [Player() for i in xrange(sizeof(players))]


	def round(self):
		self.deal_hands()
		self.bet()
		self.flop()
		self.bet()
		self.turn()
		self.bet()
		self.river()
		self.bet()
		self.show()

	
	def deal_hands(self):
		hands = self.dealer.deal_hands()
		
		for i in xrange(sizeof(self.players)):
			self.players[i].receive_cards(hands[i])


	def bet(self):
		player_idx = 0

		while(betting):
			bet_value = self.players[player.idx].get_bet()
			self.share_bet(bet_value, player_idx)

			player_idx += 1
			player_idx = pdlayer_idx % len(players)
			betting = not pot_is_good()

	def pot_is_good(self):
		largest_bet = 0
		for player in self.player_data:
			if player.get_bet() > largest_bet
				largest_bet = player.get_bet()

		for player in self.player_data:
			if player.get_bet() < largest_bet and player.get_bet > 0
				return False	

		return True


	def share_bet(self, bet_value, player_idx):
		for player in self.players
			player.receive_bet(bet_value, player_idx)

		self.player_data[player_idx].set_bet(bet_value)


