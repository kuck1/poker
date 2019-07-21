import random
from cards import Deck
# from pokerEngine import Game
from hand import Hand



x = Deck()

h = Hand([x.deal_card() for i in xrange(5)])

h.update_strength()

print(h.strength)

print([c.value for c in h.cards])
