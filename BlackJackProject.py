import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
import random

suits = ['\u2660', '\u2665', '\u2666', '\u2663']

deck_cards = (
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    )

card_values = {
    'A': 11, '2' : 2, '3' : 3, '4' : 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q' : 10, 'K': 10
    }
"""Pairs dictionary to aide in the counting funtion"""


class Card():
    """ Creating a suited card object. """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def card_type(self):
        print(f'{self.value} of {self.suit}')
        
    def face_value(self):
        if self.value == 'A': 
            'A' == 11 
        elif self.value == 'J':
            'J' == 10
        elif self.value == 'Q': 
            'Q' == 10
        elif self.value == 'K': 
            'K' == 10


class Deck():
    """ Creats a 52 deck of shuffled cards. """
    def __init__(self,):
        self.cards = []
        self.build()
        

    def build(self):
        for suit in suits:
            for value in card_values:
                self.cards.append(Card(suit, value))
    
    # not working
    # def show(self):
    #     for card in self.cards:
    #         print(f"{self.cards}")

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()

    

class Player():
    def __init__(self, player, dealer):
        self.dealer = dealer
        self.player = player
 

    def player_hand(self):
        self.hand = []
        Deck.draw()
        Deck.draw()
        print(f"\nPlayers Hand: ",{self.player_hand()}, sep='\n ')

    def dealer_hand(self):
        self.d_hand = []
        Deck.draw()
        Deck.draw()
        print("Dealer's Hand: ")
        print("*<??>*")
        print("", *self.dealer_hand[1])      

    def show(self, player, dealer):
        print("Dealer's Hand: ", *dealer.cards, sep='\n ')
        print("Dealer's Hand is: ", dealer.value)
        print("Player's Hand:", *player.cards, sep='\n ')
        print("\nPlayers Hand: ", player.value,)

    def hit(self, deck,hand):
            hand.draw(deck.deal())
            hand.adjust_ace()

    def h_or_s(deck, hand):
        while True:
            ask = input("'h' ===> HIT 's' ==> stay. Consider wisely! ")
            if ask.lower() == 'h':
                hit(deck, hand)
            elif ask.lower() == 's':
                print("You have chosen to stay. Dealers turn to play... Good luck! ")

            else:
                print("That was an invalid choice... are you sure you're 21? ")
    



"""The UI of the Game"""
def play_blackjack():
    while True:
        print("********** Created by Chelsey Martinez **********\n\n\t...Starting the game Blackjack...\n\n\tPress enter to continue")
        """Creating deck and establishing a player and dealer."""
        deck = Deck()
        deck.shuffle()
        player  = Player.player_hand()
        dealer = Player.dealer_hand()
        dealer_hand.draw(deck.deal())

        """Start of UI."""
        h_or_s(deck, player)        
        if player.value > 21:
            response = input(f"\t\tBUST with {player.value}\nCount better next time!\n\nHit enter to play again! or 'quit' ")
            if response == 'quit':
                break
            else:
                continue
        elif player.value == 21 or dealer.value:
            if player.value:
                response = input("\t\t\tPlayer has BLACKJACK!\nPress enter to play again! or 'quit' ")
                if response == 'quit':
                    break
                else:
                    continue
        elif dealer.value:
            response = input("\t\t\tDealer has BLACKJACK!\nPress enter to play again! or 'quit' ")
            if response == 'quit':
                break
            else:
                continue
        if player.value <= 21:
            while dealer.value < 17:
                dealer.hit(deck, dealer)
                show(player, dealer)
                if dealer.value > 21:
                    response = input(f"\t\t DEALER BUST with {player.value}\nPlayer Wins!\n\nHit enter to play again! or 'quit' ")
                    if response == 'quit':
                        break
                    else:
                        continue
                elif dealer.value > player.value:
                    pass
                elif dealer.value < player.value:
                    pass
            new_game = input("Would you like to play again?\n'y' ==> Yes 'n'==> no ")
            if new_game.lower == 'y':
                continue
            else:
                print("Thanks for playing! Goodbye!")
                break
                    

