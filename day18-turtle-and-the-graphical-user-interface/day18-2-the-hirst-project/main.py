#My completed version 7/31/25
# import colorgram
# colors = colorgram.extract('hirst_spots_example.jpg', 88)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_mod
import random
turtle_mod.colormode(255)
lil_turt = turtle_mod.Turtle()
lil_turt.shape("turtle")
lil_turt.penup()
lil_turt.hideturtle()
lil_turt.speed("fastest")

color_list = [(213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40),
 (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222),
 (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203),
 (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235),
 (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

lil_turt.setheading(230)
lil_turt.forward(250)
lil_turt.setheading(0)
dot_count = 100

for dots in range(1, dot_count + 1):
    lil_turt.dot(20, random.choice(color_list))
    lil_turt.forward(50)
    if dots % 10 == 0:
        lil_turt.setheading(90)
        lil_turt.forward(50)
        lil_turt.setheading(180)
        lil_turt.forward(500)
        lil_turt.setheading(0)


screen = turtle_mod.Screen()
screen.exitonclick()