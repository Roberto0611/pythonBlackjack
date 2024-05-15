# Made by: Roberto Ochoa Cuevas
from classes import deck
from classes import player

name = input("Welcome to Blackjack 21 , to start input your name\n")

gambler = player.Player(name);
dealer = player.Player("Dealer")

gambler.greetings()

while(True):
    print('game start\n')

    gambler.restartHand()
    dealer.restartHand()
    pack = deck.Deck()
    pack.shuffle()

    pack.draw(dealer)
    print("Dealer has draw a secret card")

    print(f"You draw: {pack.draw(gambler)}");

    print(f"Dealer draw: {pack.draw(dealer)}")

    print(f"You draw:{pack.draw(gambler)}");

    print(f"Your current hand: {gambler.checkHand()} with a value of: {gambler.checkHandValue()}")

    # Start game loop
    while(True):

        if(gambler.checkHandValue() == 21):
            print("BLACKJACK!!!!! YOU WIN")
            break

        action = input('\nHit or stand? ').lower()
        if action == 'hit':

            print(f"You draw:{pack.draw(gambler)}");
            print(f"Your current hand: {gambler.checkHand()} with a value of: {gambler.checkHandValue()}")
            if (gambler.checkHandValue() > 21):
                print('You bust :(');
                break
            elif( gambler.checkHandValue() == 21):
                print("BLACKJACK!!!!! YOU WIN")
                break

        elif action == 'stand':
            print('you are standing')
            break
        else:
            continue
    if(input('do you want to play again? y/n ').lower() == 'y'):
        continue
    else:
        print('Thanks for playing :)')
        break