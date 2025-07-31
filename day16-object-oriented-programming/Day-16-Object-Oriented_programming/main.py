#My completed version 07/26/25
# import turtle
# johnny = turtle.Turtle()
# print(johnny)

# from turtle import Turtle, Screen
# johnny = Turtle()
# print(johnny)
# johnny.shape("turtle")
# johnny.color('red')
# johnny.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Charizard", "Gengar", "Mew"])
table.add_column("Type", ["Electric", "Fire", "Ghost", "Psychic",])
table.add_column("Weakness",["Ground", "Water/Ground", "Psychic", "Ghost",])#<---Added new column 07/28/25
table.align = "l"



print(table)