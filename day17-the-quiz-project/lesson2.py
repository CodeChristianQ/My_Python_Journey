#Understanding Constructor.
#Constructor allows us to specify what happens to our objects when they're being constructed which in turn simplifies
# adding attributes to individual Objects. This is also known in programming as Initializing.
#Initialize - to set (variables, counters, switches,etc.) to their starting values at the beginning of a program or subprogram.
def constructor_creation():
    #Creating a constructor uses a special function.
    #Example:
    class User:
        def __init__(self): #<-- In addition to self(which is the actual Object that's being created), you can add as many parameters as you wish.
            print("New user being created...")

    user_1 = User()
    user_1.id = "0001"
    user_1.username = "Oracle"
    print(user_1.username)

    user_2 = User()
    user_1.id = "0002"
    user_1.username = "Echo"
# constructor_creation()

def constructor_creation_with_parameters():
    #Creating a constructor uses a special function.
    #Example:
    class User:
        def __init__(self, user_id, username): #<-- The parameter is going to be passed in when an Object gets constructed.
                                                #Once you receive that data you can use it to set the Objects attribute.
            self.id = user_id
            self.username = username
            print("New user being created...")

    user_1 = User("0001", "Oracle")
    user_2 = User("0002", "Echo")
    print(user_1.username)
    print(user_2.username)
# constructor_creation_with_parameters()