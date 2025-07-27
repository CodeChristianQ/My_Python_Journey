elif difficulty == "hard":
    guessing = True
    number_of_attempts = 6
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    while guessing:
        guess = int(input("Make a guess: "))
        if guess > computer_choice:
            number_of_attempts -= 1
            print("Too high!")
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        elif guess < computer_choice:
            number_of_attempts -= 1
            print("Too low!")
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        elif number_of_attempts == 0:
            guessing = False
            print("You've run out of tries! You lose! Game Over!")
        elif guess == computer_choice:
            guessing = False
            print("You guessed the right number!! You Win!!")
        else:
            number_of_attempts -= 1
            print("You have entered an incorrect input and lost an attempt, please try again")
