def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number?: "))
    continue_calculation = True

    while continue_calculation:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculation with {answer}, "
                       "type 'n' to start a new calculation, "
                       "or type 'q' to quit.\n").lower()
        if choice == 'y':
            num1 = answer
            continue_calculation = True
        elif choice == 'q':
            continue_calculation = False
        else:
            continue_calculation = False
            calculator()

calculator()
