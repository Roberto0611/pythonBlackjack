class Player:
    def __init__(self, name, startingMoney=None):
        self.name = name
        self.hand = []
        self.money = startingMoney if startingMoney is not None else 9999
        self.playerBet = 0;

        self.card_values = {'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5,'6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
            'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10,
            'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5,
            '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
            'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,
            'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5,
            '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
            'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10,
            'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
            '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
            'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10
        }

    def greetings(self):
        print(f"\nWelcome {self.name}")

    def addToHand(self,card):
        self.hand.append(card);

    def checkHand(self):
        return self.hand
    
    def checkHandValue(self):
        self.handValue = 0
        num_aces = 0

        for self.card in self.hand:
            card_value = self.card_values[self.card]
            self.handValue += card_value

            if self.card.startswith('Ace'):
                num_aces += 1

        while num_aces > 0 and self.handValue > 21:
            self.handValue -= 10  
            num_aces -= 1  

        return self.handValue
    
        # Search
    
    def restartHand(self):
        self.hand = []

    def hasBlackjack(self):
        return self.checkHandValue() == 21

    def isBusted(self):
        return self.checkHandValue() > 21    
    
    def placeBet(self,bet):
        self.playerBet = bet

    def currentMoney(self):
        return self.money;