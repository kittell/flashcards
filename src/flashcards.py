from pandas import read_excel
from random import shuffle

from flashcards_gui import FlashcardsGUI

class Application:
    def __init__(self, *args, **kwargs):
        
        # gui = FlashcardsGUI()
        # gui.mainloop()
        
        print('starting app')
        print('loading deck')
        
        return
    
    
    def add_deck(self):
        return
    
    def load_deck(self):
        return
    
    def close_deck(self):
        return
    
    def edit_deck(self):
        return


# (0) Classes
class Deck:
    """
    A Deck is a collection of flashcards.
    
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.reset_deck()
        
    def reset_deck(self):
        # Reload data
        self.df = read_excel(self.filename)
        self.df['id'] = self.df.index.tolist()
        
        # Initialize piles
        self.id_list = self.df['id'].tolist()
        self.facedown_pile = Pile(self.id_list)
        self.facedown_pile.shuffle_pile()
        self.discard_pile = Pile([])
        
    def count_remaining_cards(self):
        return self.facedown_pile.count_cards()
    
    def get_card(self):
        # Get the top card, i.e., the one at the end of the list
        card_id = self.facedown_pile.id_list[-1]
        
        # Get the row of data from self.df; convert to dict
        card_data_row = self.df[self.df['id'] == card_id]
        card_data_dict = card_data_row.to_dict(orient='records')[0]
        card = Card(card_id, card_data_dict)
        
        return card
    
    def discard(self, card):
        # Remove from facedown_pile, add to discard_pile
        self.facedown_pile.id_list.remove(card.id)
        self.discard_pile.id_list.append(card.id)

class Pile:
    def __init__(self, id_list):
        self.id_list = id_list
        
    def shuffle_pile(self):
        shuffle(self.id_list)
        
    def count_cards(self):
        return len(self.id_list)
    
class Card:
    def __init__(self, card_id, card_data):
        self.id = card_id
        self.side1 = card_data['Side 1']
        self.side2 = card_data['Side 2']
        
    def show_side(self, side):
        if side == 2:
            print(self.side2)
        else:
            print(self.side1)
    
class Round:
    def __init__(self):
        self.deck = self.select_deck()
        
    def select_deck(self):
        # TODO: hardcoding deck for now
        return Deck("flashcards_pmbok.xlsx")
    
    def play(self):
        cards_remaining = self.deck.count_remaining_cards()
        while cards_remaining > 0:
            self.take_turn()
            cards_remaining = self.deck.count_remaining_cards()
            
    def take_turn(self):
        card = self.deck.get_card()
        card.show_side(1)
        print()
        input("     Other side...")
        print()
        card.show_side(2)
        print()
        input("     Next card...")
        print()
        print()
        self.deck.discard(card)
        


# (1) Load a specific flashcards deck
app = Application()
