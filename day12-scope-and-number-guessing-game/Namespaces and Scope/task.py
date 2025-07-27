#My completed version 07/20/2025
opponents = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {opponents}")
#
# def increase_perk():
#     """The purpose of this function is to demonstrate local scope"""
#     attribute_points = 3 #<----- Local variable
#     print(attribute_points) #<---- print() function within local scope

# increase_perk()
# print(attribute_points) #<----- Notice how there is an error because the variable is not in the local scope

##Example of Global scope
total_points = 13#<-----Global scope variable outside the function

def increase_perk():
    attribute_points = 3
    print(total_points)#<----- able to use print() function for variable from Global scope from within the function. 

increase_perk()