#My completed version 07/18/2025
import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
def calculator():
    should_continue = True
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: ").lower()
        if choice == "yes":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()