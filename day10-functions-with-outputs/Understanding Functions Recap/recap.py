#🔁 Step-by-Step Hands-On Activities 07/27/2025
# TODO 1. Function Anatomy Drill Create functions with one clear purpose each. Example:
#def greet(name):
    # return f"Hello, {name}!"
# TODO a. Write the function
# TODO b. Call it with 2–3 different arguments
# TODO c. Print the result

def greet_with_name(name):
    """This function takes the argument ie(Person's name) and sets the parameter ie(name)."""
    return f"Hello {name}?"
#below are the various arguments stored in variables
person1 = greet_with_name("Christian")
person2 = greet_with_name("Kaiju")
person3 = greet_with_name("Igris")
#below we print each variable that calls the function with our various arguments.
print(person1)
print(person2)
print(person3)

def days_of_the_week(current_day):
    """This function takes the argument ie(Day of the week) and sets the parameter ie(current_day)."""
    return f"Today is {current_day}. I hope it's a good day!"
day1 = days_of_the_week("Monday")
day2 = days_of_the_week("Tuesday")
day3 = days_of_the_week("Wednesday")
print(day1)
print(day2)
print(day3)

def time_of_day(current_hour, current_minutes):
    """This function takes the argument ie(time_of_day) and sets the parameter ie(current_hour, current_minutes)."""
    return f"The time is now {current_hour}:{current_minutes}."
morning = time_of_day("08", "30")
noon = time_of_day("12", "00")
night = time_of_day("21", "00")
print(morning)
print(noon)
print(night)

# TODO 2. Parameter Practice Lab
# Make a mini calculator

def multiplying(input1, input2):
    total = input1 * input2
    if total >= 25:
        return total
    else:
        return False
equation = multiplying(5, 5)
equation2 = multiplying(4, 4)
equation3 = multiplying(3, 10)
print(equation)
print(equation2)
print(equation3)

# TODO 3. Return vs. Print Challenge
# Write a function that prints the result, and another that returns it:

def print_area(length, width):
    print(length * width)
print_area(10, 5)

def return_area(length, width):
    """This function was the breakthrough for my understanding of how powerful return actually is numerically."""
    return length * width # You're able to reuse return values for more complex variables
result = return_area(30, 10)
double = result * 5
div_by_2 = double / 2
print(div_by_2)

def my_name(first, space, last):
    return first + space + last
name = my_name("Christian", " ", "Quintero")
with_nickname = name + " aka Kaiju"
print(with_nickname)