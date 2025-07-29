#My completed solution 07/24/2025

#Todo(s) "MAIN OBJECTIVE" Create a game that compares which users have more followers on instagram, where if they guess correctly
#Todo- their score continues to accumulate until they get the answer wrong. Each correct user guess gets compared to the next random user.
#Todo(s) 1 - Where are we pulling our information from? Create or store the information from our information list into the proper variable.
#Todo(s) 1 - Set up the Import modules.
#Todo(s) 2 - Create a function that compares the 2 users.
#Todo(s) 3 - Create a function with if else conditions for what happens if the player guesses right or wrong.
#Todo(s) 4 - Create a function or variable that stores the players cumulative score if they guess correctly.
#Todo(s) 5 - (Optional) Create a function that removes previously guessed users from the original list into a already been used list, if we
        ##Todo(s) 5 -   want the game to have an end.
import random
import art
from game_data import data
# print(data[0]['name'], data[0]['description'], data[0]['country'])<---Used this to remember how getting info from dictionary and lists.

def user_data(user):
    """Formats the list output for a print function"""
    user_name = user['name']
    user_descript = user['description']
    user_country = user['country']
    return f"{user_name}, a {user_descript}, from {user_country}"

def compare_answer(player_guess, a_fans, b_fans):
    """Takes players guess and return if correct"""
    if a_fans > b_fans:
        return player_guess == "a"
    else:
        return player_guess == "b"
print(art.logo)
score = 0
continue_game = True
user_b = random.choice(data)

while continue_game:
    user_a = user_b
    user_b = random.choice(data)

    if user_a == user_b:
        user_b = random.choice(data)

    print(f"Compare A: {user_data(user_a)}")
    print(art.vs)
    print(f"Compare B: {user_data(user_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(art.logo)

    a_fans = user_a['follower_count']
    b_fans = user_b['follower_count']
    is_correct = compare_answer(guess, a_fans, b_fans)


    if is_correct:
        score =+ 1
        print(f"Your right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        continue_game = False