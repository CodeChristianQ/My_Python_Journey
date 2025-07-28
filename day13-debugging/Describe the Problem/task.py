#debug the code
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? checking if each number in the range is equal to 20
#if it is it should print the message.
# 2. When is the function meant to print "You got it"?
#for when if i in range == 20
# 3. What are your assumptions about the value of i?
#it's in a range that Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive)
#because the stop is 20 the message will never print

#My completed solution 07/22/2025

def my_function():
    for i in range(0, 21):
        if i == 20:
            print("You got it")


my_function()