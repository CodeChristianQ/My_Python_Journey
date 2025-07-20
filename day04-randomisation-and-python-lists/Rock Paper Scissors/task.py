#My completed version 07/11/2025
import random

import rps

player_choice = str(input("Let's play rock, paper, scissors! ")).lower()
if player_choice == "rock":
    print(rps.rock)
elif player_choice== "paper":
    print(rps.paper)
else:
    print(rps.scissors)
computer_options = [rps.rock, rps.paper, rps.scissors]
computer_choice = random.choice(computer_options)
print(f"Computer chose: {computer_choice}")
if player_choice == "paper" and computer_choice == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''  or player_choice == "rock" and computer_choice == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' or player_choice == "scissors" and computer_choice == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''':
 print("You win!")
elif player_choice == "paper" and computer_choice == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' or player_choice == "rock" and computer_choice == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' or player_choice == "scissors" and computer_choice == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''':
    print("It's a tie!")
else:
 print("Computer wins!")