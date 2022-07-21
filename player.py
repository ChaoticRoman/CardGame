class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def __repr__(self):
        return f"{self.name} with {self.hand}"
    
    def __test(self):
        print("test")
        
    def test(self):
        self.__test()


class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        
    def __repr__(self):
        return f"Human {Player.__repr__(self)}."
    
    def card_to_play(self):
        return self.hand[0]


class AIPlayer(Player):
    def __repr__(self):
        return "AI " + Player.__repr__(self)
    
    def card_to_play(self):
        return self.hand[-1]


if __name__ == "__main__":
    p, men, ai = Player("Unnamed"), HumanPlayer("Josef", 100), AIPlayer("T-1000")
    print((p, men, ai))
    
    players = men, ai
    for player in players:
        print(f"{player.name} plays {player.card_to_play()}")