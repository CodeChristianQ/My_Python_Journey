#My completed version 07/16/2025
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of doing something over and over again.",
}
#Pull the value of the key
# print(programming_dictionary["Bug"])
#Add a new key to dictionary
programming_dictionary["Christian"] = "The guy learning all this stuff."
# print(programming_dictionary)
#Updating / edit the definition
programming_dictionary["Bug"] = "A moth in your computer"
#Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])