#My completed version 07/12/2025
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
random_letters = ''.join(random.choices(letters, k=nr_letters))
nr_symbols = int(input(f"How many symbols would you like?\n"))
random_symbols = ''.join(random.choices(symbols, k=nr_symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_numbers = ''.join(random.choices(numbers, k=nr_numbers))

password_list = list(random_numbers + random_letters + random_symbols)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)