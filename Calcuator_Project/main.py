from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations={
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
            }
# print(operations["*"](4,8))
def initial():
    print("\n"*100)
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result} or type n to start a new calculation: ")
    if choice == "y":
        calculate_further(result)
    elif choice == "n":
        initial()

def calculate_further(result):
    num1 = result
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result} or type n to start a new calculation: ")
    if choice == "y":
        calculate_further(result)
    elif choice == "n":
        initial()

initial()






