from cards import *
from classes import *
import random as r

def populateDeck(deck, num):
	i = 0
	cards = [creeper(), zombie(), skeleton(), witch(), spider(), chargedCreeper()]
	for i in range(1,num):
		deck.addCard(r.choice(cards))
		i += 1
	return deck

populateDeck( Deck() , 20)

print(deck.draw())
print(deck.draw())

