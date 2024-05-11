class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def greetings(self):
        print(f"\nWelcome {self.name}")

    def addToHand(self,card):
        self.hand.append(card);

    def checkHand(self):
        return self.hand