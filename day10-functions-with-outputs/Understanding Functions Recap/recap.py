#🔁 Step-by-Step Hands-On Activities 07/27/2025
# TODO 1. Function Anatomy Drill Create 10 functions with one clear purpose each. Example:
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
