class Card:
    SPADES  = "Spades"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    COLORS = SPADES, HEARTS, DIAMONDS, CLUBS
    
    LOW_RANKS = tuple(str(number) for number in range(2, 11))
    HIGH_RANKS = JACK, QUEEN, KING, ACE = "Jack", "Queen", "King", "Ace"
    RANKS = LOW_RANKS + HIGH_RANKS
    
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
    
    @property
    def name(self):
        return f"{self.rank} of {self.color}"
    
    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, rank):
        rank = str(rank)
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank {rank}.")
        self._rank = rank
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        color = color.capitalize()
        if color not in self.COLORS:
            raise ValueError(f"Invalid color {color}.")
        self._color = color
    
    def rank_value(self):
        return self.RANKS.index(self._rank)

    def is_high(self):
        return self._rank in self.HIGH_RANKS

    def __eq__(self, other):
        return self._color == other._color and self._rank == other._rank
    
    def __lt__(a, b):
        """Return True if a < b"""
        return a.rank_value() < b.rank_value()
    
    def __le__(a, b):
        """Return True if a <= b"""
        return a.rank_value() <= b.rank_value()
    
    def __int__(self):
        return self.rank_value()
    
    def __repr__(self):
        return f'Card("{self._color}", "{self._rank}")'


def main():
    my_card = Card("Spades", "Ace")
    print(my_card.name)
    my_card.rank = "2"
    print(my_card.name)
    my_card.rank = 10
    print(my_card.name)
    my_card.color = "hearts"
    print(my_card.name)
    


if __name__ == "__main__":
    main()