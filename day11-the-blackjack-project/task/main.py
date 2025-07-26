#My completed version 07/19/2025- 07/20/2025
import random

import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

def player_turn():
  """This is responsible for adding random cards to the players hand."""
  random_player_card = random.choice(cards)
  player_cards.append(random_player_card)
def dealer_turn():
  """This is responsible for adding random cards to the Dealers hand."""
  random_dealer_card = random.choice(cards)
  dealer_cards.append(random_dealer_card)
def compare_outcome():
  """This is responsible for comparing dealer hand the player hand to determine a victor."""
  global continue_game
  if player_total > dealer_total:
    print(f"Your hand:{player_cards}. Your score:{player_total}. Dealer hand:{dealer_cards}. Score:{dealer_total}. You Win!")
    continue_game = False
  elif player_total < dealer_total:
    print(f"Your hand:{player_cards}. Your score:{player_total}. Dealer hand:{dealer_cards}. Score:{dealer_total}. Dealer wins!")
    continue_game = False
  elif player_total == dealer_total:
    print(f"Your hand:{player_cards}. Your score:{player_total}. Dealer hand:{dealer_cards}. Score:{dealer_total}. It's a Tie!")
    continue_game = False
  else:
    continue_game = True
def win_outcome():
  """This is responsible for determining a winner if these conditions are met."""
  global continue_game
  if player_total == 21:
    print(f"Your hand:{player_cards}. Your score:{player_total}. You Win!")
    continue_game = False
  elif dealer_total > 21:
    print(f"Dealer hand:{dealer_cards}. Score:{dealer_total}.Bust! You win!")
    continue_game = False
  elif dealer_total == 21:
    print(f"Dealer hand:{dealer_cards}. Score:{dealer_total}. Dealer Wins!")
    continue_game = False
  elif player_total > 21:
    print(f"Your hand:{player_cards}. Your score:{player_total}.Bust! Dealer wins!")
    continue_game = False
  elif player_total == 21 and dealer_total == 21:
    print(f"Your hand:{player_cards}. Your score:{player_total}. Dealer hand:{dealer_cards}. Score:{dealer_total}. It's a Tie!")
    continue_game = False

while continue_game:

  game_start = str(input("Lets play type 'y' or 'n'. ")).lower()
  if game_start == "y":
    player_cards = []
    player_total = 0
    dealer_cards = []
    dealer_total = 0
    while len(player_cards) < 2:
      player_turn()
      player_total = sum(player_cards)
    print(f"Your hand: {player_cards}. Score total: {player_total}.")
    while len(dealer_cards) < 2:
      dealer_turn()
      dealer_total = sum(dealer_cards)
    print(f"Dealers first card: {dealer_cards[0]}.")
    win_outcome()
    if not continue_game:
      break
    while player_total < 21:
      next_draw = str(input("Hit='y' or stay='n'? ")).lower()
      if next_draw == "y":
        player_turn()
        player_total = sum(player_cards)
        print(f"Your hand: {player_cards}. Score total: {player_total}.")
        win_outcome()
        if not continue_game:
          break
      else:
        break
    while dealer_total < 17:
      dealer_turn()
      dealer_total = sum(dealer_cards)

    win_outcome()
    if not continue_game:
      break
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    if continue_game:
      compare_outcome()
  else:
    print("Have a nice day!")
    continue_game = False
