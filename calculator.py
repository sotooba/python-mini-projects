# To build a calculator

VALID_OPERATORS = ["+", "-", "*", "/"]


def main():
    mode = get_mode()

    # According to mode perform calculations

    if mode == "1" or mode == "manual":
        num1, num2, operator = get_manual_input()
        calculate(num1, num2, operator)

    elif mode == "2" or mode == "expression":
        num1, num2, operator = get_expression_input()
        calculate(num1, num2, operator)

    elif mode == "3" or mode == "quit" or mode == "q":
        print("Exiting the program... Goodbye!")
    else:
        print("Invalid mode!")


# Ask the user for choice between manual or expression input

def get_mode():
    valid_mode = ["1", "2", "3", "manual", "expression", "quit", "q"]
    while True:
        mode = input(
            "Enter mode: (1)Manual, (2)Expression, (3)Quit: ").strip().lower()
        if mode in valid_mode:
            return mode
        else:
            print("Invalid mode choice!")


# Get number input from user
# Handle invalid input

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input!")


# Get operator input from user
# Handle invalid input

def get_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in VALID_OPERATORS:
            return operator
        else:
            print("Invalid operator!")


# Get manual input from user
# e.g one number at a time

def get_manual_input():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    operator = get_operator("Enter operator (+, -, *, /): ")

    return num1, num2, operator


# Get expression input from user

def get_expression_input():

    while True:
        try:
            expression = input("Enter expression (separated by space): ")
            x, op, y = expression.split()
            x, y = float(x), float(y)
            if op not in VALID_OPERATORS:
                raise ValueError
        except ValueError:
            print("Invalid input!")
        else:
            return x, y, op


# Calcualte the result of given input

def calculate(num1, num2, operator):
    if operator == "+":
        print(f"{num1} {operator} {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1} {operator} {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1} {operator} {num2} = {num1 * num2}")
    elif operator == "/":
        try:
            print(f"{num1} {operator} {num2} = {(num1 / num2):.2f}")
        except ZeroDivisionError:
            print("Real numbers divided by zero yields the output of INFINITY!")
    else:
        print("Invalid operator!")


if __name__ == "__main__":
    main()
