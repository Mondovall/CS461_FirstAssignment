# / Timothy D Hoang
#   CS 461 - Program 1/ #



import random


class Card:
    # / Card Object / #
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    # / Deck Object Creation / #
    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        for i in ["S", "C", "D", "H"]:
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

    # just to test deck values.
    def print_deck(self):
        for i in self.cards:
            print(i.value, " of ", i.suit)
    # Shuffle method for the deck
    def shuffle_cards(self):
        for i in range(len(self.cards) - 1, 0, -1):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]

    # Deal card to players
    def deal_cards(self):
        return self.cards.pop()


class Player:

    # / Player's Construction / #
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.str = ""

    # Draw card for player
    def draw_cards(self, deck):
        for i in range(0, 13):
            self.hand.append(deck.deal_cards())
        return self.hand

    #Test player's hand
    def show_hand(self):
        for i in self.hand:
            self.str += i.value + i.suit + " "
        print(self.str)


class Partner:
    # / Partner's Structure / #
    def __init__(self):
        self.hand = []

    # Method to simulate partner's hand
    def simulator_hand(self, deck):
        deck.shuffle_cards()
        for i in range(0, 13):
            self.hand.append(deck.cards[i])
        return self.hand

    def show_hand(self):
        for i in self.hand:
            print(i.suit, " ", i.value, "\n")

    # method to reset partner's hand for next simulation
    def reset_hand(self):
        self.hand = []


class Points:
    # / Structure to calculate points for both player and partner / #
    def __init__(self, hand):
        self.hand = hand
        self.total = 0

    # Method to count high cards
    def high_cards(self, index):

        if index.value == "A":
            self.total += 4
        elif index.value == "K":
            self.total += 3
        elif index.value == "Q":
            self.total += 2
        elif index.value == "J":
            self.total += 1

    # Distribution method for each points rule
    def distribution(self):
        spades = 0
        clubs = 0
        diamonds = 0
        hearts = 0

        for i in self.hand:
            if i.suit == "S":
                spades += 1
            elif i.suit == "C":
                clubs += 1
            elif i.suit == "D":
                diamonds += 1
            elif i.suit == "H":
                hearts += 1
            self.high_cards(i) # Call high card method to value each suit

        # void count
        if spades == 0 or clubs == 0 or diamonds == 0 or hearts == 0:
            self.total += 5

        # doubleton count
        if spades == 2:
            self.total += 1
        elif clubs == 2:
            self.total += 1
        elif diamonds == 2:
            self.total += 1
        elif hearts == 2:
            self.total += 1
        # singleton count
        if spades == 1:
            self.total += 2
        elif clubs == 1:
            self.total += 2
        elif diamonds == 1:
            self.total += 2
        elif hearts == 1:
            self.total += 2


def main():
    # / Main Block / #
    while True:
        thresh_hold = 1000                  # thresh hold for the simulation.
        count = 0                           # keeping track of simulation

        deck = Deck()                       # initialize a deck
        deck.shuffle_cards()
        player1 = Player("Player1")         #Initialize player
        player1.draw_cards(deck)            # player got dealt cards
        player1.show_hand()                 # Showing player's hand
        player_points = Points(player1.hand)
        player_points.distribution()
        print("Here is your hand:")
        print("This hand is worth", player_points.total, "points.")
        print("Running simulation.....\n")
        partner = Partner()                 # Initialize partner

        # Variables to keep track of each point structure.
        pass_points = 0
        part_points = 0
        game_points = 0
        small_points = 0
        grand_points = 0
        while (count >= 0) and (count <= thresh_hold):
            # Reset partner's hand each simulation then redistribute points.
            partner.reset_hand()
            partner_points = Points(partner.simulator_hand(deck))
            partner_points.distribution()
            count += 1
            game_total = player_points.total + partner_points.total

            if game_total < 20:
                pass_points += 1
            elif (game_total >= 20) and (game_total <= 25):
                part_points += 1
            elif (game_total >= 26) and (game_total <= 31):
                game_points += 1
            elif (game_total >= 32) and (game_total <= 35):
                small_points += 1
            elif game_total >= 36:
                grand_points += 1

        # Calculate and Display probabilities.
        print("The estimated probability base on ", thresh_hold, "simulated hands")
        print("Pass: ", "{:.1f}%".format((pass_points / thresh_hold) * 100))
        print("Part score: ", "{:.1f}%".format((part_points / thresh_hold) * 100))
        print("Game: ", "{:.1f}%".format((game_points / thresh_hold) * 100))
        print("Small Slam: ", "{:.1f}%".format((small_points / thresh_hold) * 100))
        print("Grand Slam: ", "{:.1f}%".format((grand_points / thresh_hold) * 100))
        if count > thresh_hold:
            player_input = input(str("\nAnother hand[Y/N]? "))
            if player_input.lower() == "y":
                True
            elif player_input.lower() == "n":
                exit(1)
            else:
                print("Input error, terminating simulation.")
                exit(1)


if __name__ == "__main__":
    main()
