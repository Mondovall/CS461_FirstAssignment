import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1, 14):
                if j == 1:
                    self.cards.append(Card("A", i))
                elif j == 11:
                    self.cards.append(Card("J", i))
                elif j == 12:
                    self.cards.append(Card("Q", i))
                elif j == 13:
                    self.cards.append(Card("K", i))
                else:
                    self.cards.append(Card(str(j), i))

    def print_deck(self):
        for i in self.cards:
            print(i.value, " of ", i.suit)

    def shuffle_cards(self):
        for i in range(len(self.cards) -1, 0, -1):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]

    def deal_cards(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw_cards(self, deck):
        for i in range(0, 13):
            self.hand.append(deck.deal_cards())
        return self.hand

    def show_hand(self):
        for i in self.hand:
            print(i.value, i.suit, "\n")


class Points():
    def __init__(self, player):
        self.player = player
        self.total_high_cards = 0
        self.total_distribution = 0
        self.total = self.total_distribution + self.total_high_cards

    def high_cards(self):

        for i in self.player.hand:
            if i.value == "A":
                self.total_high_cards += 4
            elif i.value == "K":
                self.total_high_cards += 3
            elif i.value == "Q":
                self.total_high_cards += 2
            elif i.value == "J":
                self.total_high_cards += 1


    def distribution(self):
        spades = 0
        clubs = 0
        diamonds = 0
        hearts = 0

        for i in self.player.hand:
            if i.suit == "Spades":
                spades += 1
            elif i.suit == "Clubs":
                clubs += 1
            elif i.suit == "Diamonds":
                diamonds += 1
            elif i.suit == "Hearts":
                hearts += 1

        # need to put in a function
        if spades == 0 or clubs == 0 or diamonds == 0 or hearts ==0:
            self.total_distribution += 5

        # need to put in a function
        if spades == 2:
            self.total_distribution += 1
        elif clubs == 2:
            self.total_distribution += 1
        elif diamonds == 2:
            self.total_distribution += 1
        elif hearts == 2:
            self.total_distribution += 1
        # need to put in a function
        if spades == 1:
            self.total_distribution += 2
        elif clubs == 1:
            self.total_distribution += 2
        elif diamonds == 1:
            self.total_distribution += 2
        elif hearts == 1:
            self.total_distribution += 2


deck = Deck()
deck.shuffle_cards()
player1 = Player("Player1")
player1.draw_cards(deck)
player1.show_hand()
points = Points(player1)
points.distribution()
points.high_cards()
print("points is: ", points.total_high_cards)










