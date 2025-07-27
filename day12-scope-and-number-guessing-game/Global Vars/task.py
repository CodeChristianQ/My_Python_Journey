#My completed version 07/21/2025
# Modifying Global Scope

opponents = 2

def new_enemies1():
    global opponents #<---- Tapping into a Global Scoped variable that is defied outside the function.
    opponents += 1
    print(f"enemies inside function: {opponents}")


new_enemies1()
print(f"enemies outside function: {opponents}")

#Instead of modifying the enemies like the example above. Let's return them instead.

def new_enemies2(opponents):
    print(f"enemies inside function: {opponents}")
    return opponents + 1

opponents = new_enemies2(opponents)
print(f"enemies outside function: {opponents}")
