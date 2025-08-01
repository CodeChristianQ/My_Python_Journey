#My completed version 07/29/25

#For all classes we use what is called PascalCase.
#Example : ThisIsPascalCase <--- Notice how each starting letter in the class is capitalized.
#This is different from camelCase and snake_case.
#Where camelCase = the first word always being lower case and every word after capitalized.
#Where snake_case = all lower case with underscores separating each word.

#Creating classes and objects.
#To create a class we use class followed by the name of the class.
def class_creation():
    #Example:
    class User:
        pass  #<--- This is used if you have an empty class or function so there is no indentation error on the next line.
    user_1 = User()
    # How do we add attributes? What is an attribute?
    #Example:
    user_1.id = "0001"
    user_1.username = "Oracle"
    #An attribute is a variable that is associated with an Object. These are the "Things" that the Object will have.
    # Now id = 0001 and username = Oracle, and we can use these attributes with our code.
    # Example:
    print(user_1.username)
# class_creation()


