import random
import cardClass

class Deck:
  '''
  Creates a list with the deck of cards inside of it

  Methods:
  - shuffle
  - deal
  '''
  def __init__(self):
    self.cards = []
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    ranks = [
            {'rank': 'A', 'value': '11'},
            {'rank': '1', 'value': '1'},
            {'rank': '2', 'value': '2'},
            {'rank': '3', 'value': '3'},
            {'rank': '4', 'value': '4'},
            {'rank': '5', 'value': '5'},
            {'rank': '6', 'value': '6'},
            {'rank': '7', 'value': '7'},
            {'rank': '8', 'value': '8'},
            {'rank': '9', 'value': '9'},
            {'rank': '10', 'value': '10'},
            {'rank': 'J', 'value': '10'},
            {'rank': 'Q', 'value': '10'},
            {'rank': 'K', 'value': '10'},
            ]
    
    for suit in suits:
      for rank in ranks:
        self.cards.append(cardClass.Card(suit, rank))
  
  def shuffle(self):
    '''Shuffles the deck of cards if the length of the list is greater than 1'''
    if (len(self.cards) > 1):
      random.shuffle(self.cards)
  
  def deal(self, number):
    '''
    Removes a given number of cards from the deck and returns them as a list
    only if the deck is not empty.  
    '''
    cards_dealt = []
    for _ in range(number):
      if len(self.cards) > 0:
        cards_dealt.append(self.cards.pop())
    return cards_dealt