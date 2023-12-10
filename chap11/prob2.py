import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['h', 'd', 'c', 's']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        hand_str = "\t".join(map(str, self.hand))
        total = self.calculate_total()
        return f"{self.name}: {hand_str}\t<{total}>"

    def calculate_total(self):
        total = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank == 'A':
                total += 11
            else:
                total += int(card.rank)

        # Adjust for Aces
        for card in self.hand:
            if card.rank == 'A' and total > 21:
                total -= 10
        return total

class BlackjackGame:
    def __init__(self, num_players):
        self.players = [Player(input("Enter player name: ")) for _ in range(num_players)]
        self.dealer = Player("Dealer")
        self.deck = Deck()

    def initial_deal(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                player.hand.append(self.deck.deal())

    def play_round(self):
        for player in self.players:
            while True:
                print(player)
                choice = input(f"{player.name}, do you want a hit? (Y/N): ").lower()
                if choice == 'y':
                    player.hand.append(self.deck.deal())
                    if player.calculate_total() > 21:
                        print(f"{player.name} busts.")
                        break
                else:
                    break

        while self.dealer.calculate_total() < 17:
            self.dealer.hand.append(self.deck.deal())

        print(f"\n{self.dealer}")

        for player in self.players:
            if player.calculate_total() > 21:
                print(f"{player.name} loses.")
            elif self.dealer.calculate_total() > 21 or player.calculate_total() > self.dealer.calculate_total():
                print(f"{player.name} wins.")
            elif player.calculate_total() < self.dealer.calculate_total():
                print(f"{player.name} loses.")
            else:
                print(f"{player.name} pushes.")

    def play(self):
        

        while True:
            self.initial_deal()
            self.play_round()

            play_again = input("\nDo you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    print("            Welcome to Blackjack!\n")
    num_players = int(input("How many players? (1-7): "))
    game = BlackjackGame(num_players)
    game.play()