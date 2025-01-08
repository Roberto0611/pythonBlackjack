from classes import deck
from classes import player
from classes.records import *

class Game:
    def __init__(self):

        if returnRecord()[1] != "noRecord":
            print("Welcome to Blackjack 21, this are the actual records:")
            print(checkRecord())
        else:
            print("Welcome to Blackjack 21")

        self.gambler = player.Player(input("To start input your name\n"),100)
        self.dealer = player.Player("Dealer")
        self.pack = deck.Deck()

    def start_game(self):
        self.gambler.greetings();
        while True:
            print("Game start")

            # Place bets
            print(f"{self.gambler.name}'s Current money: {self.gambler.currentMoney()}$")

            if self.gambler.currentMoney() == 0:
                print("Sorry you don't have enough money to play :(")
                break

            while True:
                self.gambler.placeBet(int(input('Place your bet $')));
                if self.gambler.playerBet > self.gambler.money:
                    print(f'Not enough money, your current balance is {self.gambler.money}')
                    continue
                else:
                    self.gambler.money -= self.gambler.playerBet
                    break

            self.setup_round()
            self.player_turn()

            if self.gambler.isBusted() or self.gambler.hasBlackjack():
                pass
            else:
                self.dealer_turn()

            if not self.play_again():
                    # Check the record returnRecord()[1]
                    if returnRecord()[1] == "noRecord" or self.gambler.money > int(returnRecord()[1]):
                        stablishRecord(self.gambler.name,self.gambler.money)
                        print(f'NEW RECORD REGISTERED!!, Thanks for playing :), your currency was {self.gambler.money}')
                    print(f'Thanks for playing :), your currency was {self.gambler.money}')
                    input("click any key to exit")
                    break
    
    def setup_round(self):
        
        # Restart hands
        self.gambler.restartHand()
        self.dealer.restartHand()

        # Open new deck
        self.pack = deck.Deck()
        self.pack.shuffle()
        
        # deal cards
        self.pack.draw(self.dealer)
        
        print("Dealer has draw a secret card")

        print(f"You draw: {self.pack.draw(self.gambler)}")
    
        print(f"Dealer draw: {self.pack.draw(self.dealer)}")

        print(f"You draw:{self.pack.draw(self.gambler)}")

        print(f"Your current hand: {self.gambler.checkHand()} with a value of: {self.gambler.checkHandValue()}")

    def player_turn(self):
        while True:
         if self.gambler.hasBlackjack():
            print("BLACKJACK!! YOU WIN!")
            self.check_winner()
            break
         elif self.gambler.isBusted():
            print("You are busted :(")
            self.check_winner()
            break
         else:
            action = input("\nHit or stand? ").lower()

            if action == "hit":
                print(f"You draw:{self.pack.draw(self.gambler)}");
                print(f"Your current hand: {self.gambler.checkHand()} with a value of: {self.gambler.checkHandValue()}")
                continue
            elif action == "stand":
                print('you are standing');
                break
    
    def dealer_turn(self):
        while True:
            if self.dealer.hasBlackjack():
                print('DEALER HAS BLACKJACK!')
                self.check_winner()
                break
            elif self.dealer.isBusted():
                print("Dealer is busted!")
                self.check_winner()
                break
            elif self.dealer.checkHandValue() < 17:
                print(f"Dealer draw:{self.pack.draw(self.dealer)}");
                continue
            elif self.dealer.checkHandValue() >= 17:
                print('Dealer is standing')
                self.check_winner()
                break

    def check_winner(self):
        if self.gambler.isBusted():
            print(f"Dealer hand: {self.dealer.checkHand()} with a value of: {self.dealer.checkHandValue()}")
            print("\nDealer wins")
        elif self.dealer.isBusted() or self.gambler.checkHandValue() > self.dealer.checkHandValue():
            print(f"Dealer hand: {self.dealer.checkHand()} with a value of: {self.dealer.checkHandValue()}")            
            print(f"\nYou win!!, bet reward: {self.gambler.playerBet * 2}")
            self.gambler.money += self.gambler.playerBet * 2
        elif self.gambler.checkHandValue() < self.dealer.checkHandValue():
            print(f"Dealer hand: {self.dealer.checkHand()} with a value of: {self.dealer.checkHandValue()}")
            print('\nDealer wins!!')
        else:
            print(f"Dealer hand: {self.dealer.checkHand()} with a value of: {self.dealer.checkHandValue()}")
            print(f"\nIt's a tie!, you get your bet back: {self.gambler.playerBet}")
            self.gambler.money += self.gambler.playerBet
    
    def play_again(self):
        return input("\nDo you want to play again? y/n ").lower() == 'y'