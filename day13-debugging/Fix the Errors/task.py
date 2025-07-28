#My completed solution 07/23/2025
#Here we'll learn about the try except block.
#This code block throws up a value error. Solution below.
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#Solution
try:
    age = int(input("How old are you?")) #If we write a string as the answer, this allows our user to try again.
except ValueError:
    print("You've entered the wrong type of input, Try a numerical digit.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")