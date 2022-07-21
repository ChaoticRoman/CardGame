import random

from player import HumanPlayer, AIPlayer
from card import Card

deck = [
    Card(color, rank)
    for color in Card.COLORS
    for rank in Card.RANKS
]

random.shuffle(deck)

for card in deck:
    print(card)
    
player = HumanPlayer("Pepa")
for _ in range(5):
    player.hand.append(deck.pop())
    
    
print(player)
for card in deck:
    print(card)
    
    
class GameOfPrsi():
    def __init__(self, players):
        self.players = players