#My completed version 07/10/2025
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Let's play a treasure hunt adventure game.")
print("In this game, your decisions will affect the outcome.")
print("Make the wrong decision and it's Game Over. You have to start over!")

choice1 = str(input("Do you wish to continue? Type yes or no ")).lower()
if choice1 == "yes":
  choice2 = str(input("It's a scolding hot summer day. You wake up on a highway and you're only able to go north or south. Type north or south. ")).lower()
  if choice2 == "north":
    choice3 = str(input("After walking north for hours you find a car with the keys in it and nobody around. Do you steal the car or do you keep walking? Type drive or walk ")).lower()
    if choice3 == "drive":
      print("You get in the car and start driving. You hear a strange noise and the car blows up! Game Over!")
    elif choice3 == "walk":
      print("You continue to walk for another hour and but pass out from dehydration. There is no one around that can help you and you pass. Game Over!")
    else:
      print("Game Over! Start Over!")
  elif choice2 == "south":
    choice4 = str(input("After walking south for hours you finally reach a lake with an island in the middle. There is a boat off in the distance heading toward you at the slowest possible speed. Do you swim or wait? ")).lower()
    if choice4 == "swim":
      choice5 = str(input("After swimming for what seems like forever you finally reach the island. There is a building with 3 doors. A yellow one a blue one and a red one. which door do you go through? Type yellow, blue, or red. ")).lower()
      if choice5 == "yellow":
        choice6 = str(input("You open the door and walk in there is a podium with 2 buttons a green one and a purple one. Which one do you press? Type green or purple. ")).lower()
        if choice6 == "green":
          print("After pushing the button a hidden door opens at the back of the room. You walk in to find a lifetime worth of treasure! Congratulations! You win and have found the treasure!")
        elif choice6 == "purple":
          print("After pushing the button spikes come out of the ground terminating you. Game Over!")
        else:
          print("Game Over! Start Over!")
      elif choice5 == "red":
        choice7 = str(input("You walk in and there is 2 more doors one is metal and the other is wood. Which do you choose to walk through? Type metal or wood. "))
        if choice7 == "wood":
          print("You walk in and get assassinated. Game Over!")
        elif choice7 == "metal":
          print("You walk through the door and fall down a hole you didn't see to your death. Game Over!")
      else:
        print("Game Over! Start Over!")
    else:
      print("You board the boat and head towards the island. On the trip you realize the crew on the boat are pirates. They steal your booty and make you walk the plank. Game Over!")
else:
  print("Game Over! Start Over!")