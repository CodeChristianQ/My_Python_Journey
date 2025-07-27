#My completed version 07/21/2025
# There is no Block Scope in Python!

round_level = 3
opponents = ["Nords", "Ogres", "Khajit", ] #<----Global Scope

def add_enemy():
    new_enemy = ""#<---- Local Scope
    if round_level < 5:
        new_enemy = opponents[3]#<---- Accessed from the Global Scope

    print(new_enemy)#<---- will only run if located in same block as variable which is Local Scope