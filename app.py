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


class Partner():
    def __init__(self):
        self.hand = []

    def simulator_hand(self, deck):
        deck.shuffle_cards()
        for i in range(0, 13):
            self.hand.append(deck.cards[i])
        return self.hand

    def show_hand(self):
        for i in self.hand:
            print(i.suit, " ", i.value, "\n")


class Points():
    def __init__(self, hand):
        self.hand = hand
        self.total= 0

    def high_cards(self, index):

        if index.value == "A":
            self.total += 4
        elif index.value == "K":
            self.total += 3
        elif index.value == "Q":
            self.total += 2
        elif index.value == "J":
            self.total += 1

    def distribution(self):
        spades = 0
        clubs = 0
        diamonds = 0
        hearts = 0

        for i in self.hand:
            if i.suit == "Spades":
                spades += 1
            elif i.suit == "Clubs":
                clubs += 1
            elif i.suit == "Diamonds":
                diamonds += 1
            elif i.suit == "Hearts":
                hearts += 1
            self.high_cards(i)

        # need to put in a function
        if spades == 0 or clubs == 0 or diamonds == 0 or hearts ==0:
            self.total += 5

        # need to put in a function
        if spades == 2:
            self.total += 1
        elif clubs == 2:
            self.total += 1
        elif diamonds == 2:
            self.total += 1
        elif hearts == 2:
            self.total += 1
        # need to put in a function
        if spades == 1:
            self.total += 2
        elif clubs == 1:
            self.total += 2
        elif diamonds == 1:
            self.total += 2
        elif hearts == 1:
            self.total += 2
# variable declarations
thresh_hold = 500
count = 0
pass_points = 0
part_points = 0
game_points = 0
small_points = 0
grand_points = 0
play_again = True
player_input = "y"

deck = Deck()
deck.shuffle_cards()
player1 = Player("Player1")
player1.draw_cards(deck)
player1.show_hand()
points = Points(player1.hand)
points.distribution()
partner = Partner()
while play_again:
    while (count >= 0) and (count <= thresh_hold):
        total = 0
        partner_points = Points(partner.simulator_hand(deck))
        partner_points.distribution()
        count += 1
        total = points.total + partner_points.total

        if total < 20:
            pass_points += 1
        elif (total >= 20) and (total <= 25):
            part_points += 1
        elif (total <= 26) and (total <= 31):
            game_points += 1
        elif (total <= 32) and (total <= 35):
            small_points += 1
        elif total >= 36:
            grand_points += 1
    print("The estimated probability base on ", thresh_hold, "simulated hands")
    print("Pass: ", (pass_points / thresh_hold) * 100)
    print("Part score: ", (part_points / thresh_hold) * 100)
    print("Game: ", (game_points / thresh_hold) * 100)
    print("Small Slam: ", (small_points / thresh_hold) * 100)
    print("Grand Slam: ", (grand_points / thresh_hold) * 100)
    if count > thresh_hold:
        # print("The estimated probability base on ", thresh_hold, " simulated hands")
        # print("Pass: ", (pass_points / thresh_hold) * 100)
        # print("Part score: ", (part_points / thresh_hold) * 100)
        # print("Game: ", (game_points / thresh_hold) * 100)
        # print("Small Slam: ", (small_points / thresh_hold) * 100)
        # print("Grand Slam: ", (grand_points / thresh_hold) * 100)
        player_input = input(str("Another hand[Y/N]? "))
        if player_input.lower() == "y":
            count = 0
            play_again = True
        elif player_input.lower() == "n":
            exit(1)
        else:
            player_input = input(str("Not the right input [Y/N]? "))



