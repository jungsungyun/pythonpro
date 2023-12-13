#(1)
import random

class PositionableCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['s', 'h', 'd', 'c']
        self.cards = [PositionableCard(rank, suit) for rank in ranks for suit in suits]

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ['K', 'Q', 'J']:
                value += 10
            elif card.rank == 'A':
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

class Dealer:
    def __init__(self):
        self.hand = Hand()

class BJ_Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = [Player(input("Enter player name: ")) for _ in range(num_players)]

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                card = random.choice(self.deck.cards)
                self.deck.cards.remove(card)
                player.hand.add_card(card)

    def display_game_state(self, player):
        print(f"{player.name}: ", end='')
        for card in player.hand.cards:
            print(f"{card.rank}{card.suit} ", end='')
        print(f"<{player.hand.get_value()}>", end='  ')

    def play_game(self):
        


        while True:
            self.deal_initial_cards()

            for player in self.players:
                while input(f"\n{player.name}, do you want a hit? (Y/N): ").lower() == 'y':
                    card = random.choice(self.deck.cards)
                    self.deck.cards.remove(card)
                    player.hand.add_card(card)
                    self.display_game_state(player)
                    if player.hand.get_value() > 21:
                        print(f"\n{player.name} busts.")
                        break

            while self.dealer.hand.get_value() < 17:
                card = random.choice(self.deck.cards)
                self.deck.cards.remove(card)
                self.dealer.hand.add_card(card)

            print("\nDealer:", end = " ")
            for card in self.dealer.hand.cards:
                print(f"{card.rank}{card.suit}", end = " ")
            print(f"<{self.dealer.hand.get_value()}>")

            for player in self.players:
                if player.hand.get_value() > 21:
                    print(f"{player.name} loses.")
                elif self.dealer.hand.get_value() > 21 or player.hand.get_value() > self.dealer.hand.get_value():
                    print(f"{player.name} wins.")
                elif player.hand.get_value() == self.dealer.hand.get_value():
                    print(f"{player.name} ties with the dealer.")

            play_again = input("\nDo you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                break
print("             Welcome to Blackjack!\n")
num_players = int(input("How many players? (1-7): "))
game = BJ_Game(num_players)
game.play_game()

#(2)
import random

class PositionableCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank,self.suit
class Card:
    def __init__(self):
        suits = ['h', 'd', 'c', 's']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [PositionableCard(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        hand_str = "\t".join(map(str, self.hand))
        total = self.calculate_total()
        return self.name,hand_str,total

    def calculate_total(self):
        total = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank == 'A':
                total += 11
            else:
                total += int(card.rank)
        for card in self.hand:
            if card.rank == 'A' and total > 21:
                total -= 10
        return total

class BlackjackGame:
    def __init__(self, num_players):
        self.players = [Player(input("Enter player name: ")) for _ in range(num_players)]
        self.dealer = Player("Dealer")
        self.deck = Card()

    def initial_deal(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                player.hand.append(self.deck.deal())

    def play_round(self):
        for player in self.players:
            while True:
                print(player)
                choice = input(player.name, "do you want a hit? (Y/N): ").lower()
                if choice == 'y':
                    player.hand.append(self.deck.deal())
                    if player.calculate_total() > 21:
                        print(player.name, "busts.")
                        break
                else:
                    break

        while self.dealer.calculate_total() < 17:
            self.dealer.hand.append(self.deck.deal())

        print(self.dealer)

        for player in self.players:
            if player.calculate_total() > 21:
                print(player.name, "loses.")
            elif self.dealer.calculate_total() > 21 or player.calculate_total() > self.dealer.calculate_total():
                print(player.name," wins.")
            elif player.calculate_total() < self.dealer.calculate_total():
                print(player.name, "loses.")
            else:
                print(player.name, "pushes.")

    def play(self):
        

        while True:
            self.initial_deal()
            self.play_round()

            play_again = input("\nDo you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                break


print("            Welcome to Blackjack!\n")
num_players = int(input("How many players? (1-7): "))
game = BlackjackGame(num_players)
game.play()

#(3)
class PositionableCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank,self.suit
class Card:
    def __init__(self):
        suits = ['h', 'd', 'c', 's']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [PositionableCard(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)