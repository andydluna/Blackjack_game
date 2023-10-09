import deckClass
import handClass

class Game:
  '''
  Allows for the blackjack game to run a given number of times. 

  Methods:
  - play
  - check_winner
  '''
  def play(self):
    '''
    Runs the game a given number of times. For each game, it creates a new Deck
    of cards, shuffles them, creates a new Hand for the player and the dealer,
    and adds two cards to each hand. 

    The program asks the user whether to stand or hit and determines as the winner 
    using the check_winner method.
    '''
    game_number = 0
    games_to_play = 0
    
    while games_to_play <= 0:
      try:
        games_to_play = int(input('how many games do you want to play? '))
      except:
        print('You must enter a number!')

    while game_number < games_to_play:
      game_number += 1
      deck = deckClass.Deck()
      deck.shuffle()
      player_hand = handClass.Hand()
      dealer_hand = handClass.Hand(dealer=True)

      for _ in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print()
      print('*' * 30)
      print(f'Game {game_number} of {games_to_play}')
      print('*' * 30)

      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      choice = ""
      while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
        choice = input("Please chose 'Hit' or 'Stand': ").lower()
        print()
        while choice not in ['s', 'h', 'stand', 'hit']:
          choice = input("Please chose 'Hit' or 'Stand' (or H/S): ").lower()
          print()
        if choice in ['h', 'hit']:
          player_hand.add_card(deck.deal(1))
          player_hand.display()
          
      if self.check_winner(player_hand, dealer_hand):
          continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()
      
      dealer_hand.display(show_all_dealer_cards=True)
      
      if self.check_winner(player_hand, dealer_hand):
        continue

      print('Final results:')
      print('Your hand', player_hand_value)
      print("Dealer's hand", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print('\nThanks for playing!')
      
  def check_winner(self, player_hand, dealer_hand, game_over=False):
    '''Determines the winner using standard blackjack rules'''
    if not game_over:
      if player_hand.get_value() > 21: 
        print('You busted. Dealer wins!')
        return True
      elif dealer_hand.get_value() > 21:
        print('Dealer busted. You win!')
        return True
      elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
        print('Both players have blackjacks! Tie!')
        return True
      elif dealer_hand.is_blackjack():
        print('Dealer has blackjack. Dealer wins!')
        return True
      elif player_hand.is_blackjack():
        print('You have blackjack. You win!')
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print('You win!')
      elif dealer_hand.get_value() == player_hand.get_value():
        print('Tie!')
      else:
        print('Dealer wins!')
    return False