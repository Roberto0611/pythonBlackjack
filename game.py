# Made by: Roberto Ochoa Cuevas
from classes import deck
from classes import player

name = input("Welcome to Blackjack 21 , to start input your name\n")

gambler = player.Player(name);
dealer = player.Player("Dealer")

gambler.greetings()

print('game start')


deck = deck.Deck()
deck.shuffle();

print(f"Dealer draw: {deck.draw(dealer)}")

print(f"You draw: {deck.draw(gambler)}");

deck.draw(dealer)
print("Dealer has draw a secret card")

print(f"You draw:{deck.draw(gambler)}");

print(f"Your current hand: {gambler.checkHand()}")