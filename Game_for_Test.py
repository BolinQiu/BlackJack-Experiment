import random

suits = (
    "Hearts",
    "Diamonds",
    "Spades",
    "Clubs",
)
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.deck *= 3

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n " + card.__str__()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 10000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# def take_bet(chips):
#     while True:
#         try:
#             chips.bet = int(input("How many chips would you like to bet? "))
#         except ValueError:
#             print("Your bet must be an integer! Try again.")
#         else:
#             if chips.bet > chips.total or chips.bet <= 0:
#                 print(
#                     "Your bet cannot exceed your balance and you have to enter a positive bet! Your current balance is: ",
#                     chips.total,
#                 )
#             else:
#                 break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# def hit_or_stand(deck, hand):
#     global playing
#
#     while True:
#         x = input("Would you like to Hit or Stand? Enter '1' or '0' ")
#
#         if x.lower() == "1":
#             hit(deck, hand)
#
#         elif x.lower() == "0":
#             print("You chose to stand. Dealer will hit.")
#             playing = False
#
#         else:
#             print("Wrong input, please try again.")
#             continue
#         break


# def show_some(player, dealer):
#     print("\nDealer's Hand:")
#     print(" { hidden card }")
#     print("", dealer.cards[1])
#     print("\nYour Hand:", *player.cards, sep="\n ")


# def show_all(player, dealer):
#     print("\nDealer's Hand:", *dealer.cards, sep="\n ")
#     print("Dealer's Hand =", dealer.value)
#     print("\nYour Hand:", *player.cards, sep="\n ")
#     print("Your Hand =", player.value)


def player_busts(player, dealer, chips):
    # print("You are BUSTED !")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    # print("You are the winner!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    # print("Dealer has BUSTED !")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    # print("Dealer is the winner!")
    chips.lose_bet()


def push(player, dealer):
    print("The match is tie !")


def Simulator(Times, Target):
    global playing
    WIN = 0
    LOSS = 0
    TIE = 0
    player_chips = Chips()
    while True:
        Times -= 1
        deck = Deck()  # 创建一副牌
        deck.shuffle()

        player_hand = Hand()  # 闲家手，发两张牌
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()  # 庄家手，发两张牌
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # take_bet(player_chips)  # 设置bet

        # show_some(player_hand, dealer_hand)  # 看牌

        while playing:  # 跟还是不跟

            while player_hand.value < Target:
                hit(deck, player_hand)
            # show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                LOSS += 1
            break

        if player_hand.value <= 21:  # 庄家跟牌，判断输赢

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                # dealer_busts(player_hand, dealer_hand, player_chips)
                WIN += 1

            elif dealer_hand.value > player_hand.value:
                # dealer_wins(player_hand, dealer_hand, player_chips)
                LOSS += 1

            elif dealer_hand.value < player_hand.value:
                # player_wins(player_hand, dealer_hand, player_chips)
                WIN += 1

            else:
                # push(player_hand, dealer_hand)
                TIE += 1
        # print("\nYour current balance stands at", player_chips.total)

        if player_chips.total > 0:  # 继续与否
            if Times > 0:
                playing = True
                continue
            else:
                break
        else:
            break
    return WIN, LOSS, TIE
