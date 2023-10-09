class Hand:
  '''
  Creates a hand of cards for either the player or the dealer. Takes in a bool which 
  determines if the hand is from a player or the dealer.  

  Methods:
  - add_card
  - calculate_value
  - get_value
  - is_blackjack
  - display
  '''
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list):
    '''Adds a given list of cards to the hand'''
    self.cards.extend(card_list)

  def calculate_value(self):
    '''Calculates the value of all the cards in the hand'''
    self.value = 0
    has_ace = False
    for card in self.cards:
      card_value = int(card.rank['value'])
      self.value += card_value
      if card.rank['rank'] == 'A':
        has_ace += True

    if has_ace and self.value > 21:
      self.value -= 10

  def get_value(self):
    '''Returns the value of all the cards in the hand'''
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    '''Returns true if the value of the cards is exactly 21, otherwise returns False'''
    return self.get_value() == 21

  def display(self, show_all_dealer_cards=False):
    '''
    Displays the cards in the hand. If it is the dealer's hand, 
    shows the first card as hidden. 
    '''
    print(f'''{"Dealer's" if self.dealer else 'Your'} hand:''')
    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer \
      and not show_all_dealer_cards and not self.is_blackjack():
        print('Hidden')
      else:
        print(card)

    if not self.dealer:
      print('Value:', self.get_value())
    print()