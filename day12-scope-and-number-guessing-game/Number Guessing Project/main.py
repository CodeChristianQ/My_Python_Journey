#My completed guided version 07/22/2025

from random import randint

easy_number_of_attempts = 12
hard_number_of_attempts = 6

def check_result(player_guess, computer_number, attempts):
    if player_guess > computer_number:
        print("Too High!")
        return attempts -1
    elif player_guess < computer_number:
        print("Too low!")
        return attempts -1
    else:
        print(f"You got the answer! It was {computer_number}")

def setting_difficulty():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if difficulty == "easy":
        return easy_number_of_attempts
    else:
        return hard_number_of_attempts

def guessing_game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = randint(1, 100)

    attempts = setting_difficulty()

    guess = 0
    while guess != computer_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_result(guess, computer_number, attempts)
        if attempts == 0:
            print("You've run out of turns, You Lose!")
            return

guessing_game()


#My completed version
import random

# computer_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23,
#                     24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
#                     46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
#                     68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
#                     90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# gaming = True
# while gaming:
#     computer_choice = random.choice(computer_numbers)
#     print("I'm thinking of a number between 1 and 100.")
#     print(computer_choice)
#     difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
#     if difficulty == "easy":
#         guessing = True
#         number_of_attempts = 15
#         print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#
#         while guessing:
#             guess = int(input("Make a guess: "))
#             if number_of_attempts < 2:
#                 guessing = False
#                 print("You've run out of tries! You lose! Game Over!")
#                 keep_playing = input("Keep playing? Type 'y' or 'n': ").lower()
#                 if keep_playing == "n":
#                     gaming = False
#                     print("Have a nice day!")
#             elif int(guess) > computer_choice:
#                 number_of_attempts -= 1
#                 print("Too high!")
#                 print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#             elif int(guess) < computer_choice:
#                 number_of_attempts -= 1
#                 print("Too low!")
#                 print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#             elif int(guess) == computer_choice:
#                 guessing = False
#                 print("You guessed the right number!! You Win!!")
#                 keep_playing = input("Keep playing? Type 'y' or 'n': ").lower()
#                 if keep_playing == "n":
#                     gaming = False
#                     print("Have a nice day!")
#             else:
#                 number_of_attempts -= 1
#                 print("You have entered an incorrect input and lost an attempt, please try again")
#     elif difficulty == "hard":
#         guessing = True
#         number_of_attempts = 7
#         print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#
#         while guessing:
#             guess = int(input("Make a guess: "))
#             if number_of_attempts < 2:
#                 guessing = False
#                 print("You've run out of tries! You lose! Game Over!")
#                 keep_playing = input("Keep playing? Type 'y' or 'n': ").lower()
#                 if keep_playing == "n":
#                     gaming = False
#                     print("Have a nice day!")
#             elif guess > computer_choice:
#                 number_of_attempts -= 1
#                 print("Too high!")
#                 print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#             elif guess < computer_choice:
#                 number_of_attempts -= 1
#                 print("Too low!")
#                 print(f"You have {number_of_attempts} attempts remaining to guess the number.")
#             elif guess == computer_choice:
#                 guessing = False
#                 print("You guessed the right number!! You Win!!")
#                 keep_playing = input("Keep playing? Type 'y' or 'n': ").lower()
#                 if keep_playing == "n":
#                     gaming = False
#                     print("Have a nice day!")
#             else:
#                 number_of_attempts -= 1
#                 print("You have entered an incorrect input and lost an attempt, please try again")
#     else:
#         print("You have selected an invalid input. Please try again.")
#         option = str(input("Do you wish to continue? Type 'y' or 'n': ")).lower()
#         if option == "n":
#             gaming = False
#             print("Have a nice day!")