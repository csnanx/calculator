import art

def add(num_1, num_2):
    return num_1 + num_2
def subtract(num_1, num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2
def divide(num_1, num_2):
    return num_1 / num_2

def calculate(num_1, num_2):
    if operation == "+":
        return add(num_1, num_2)
    elif operation == "-":
        return subtract(num_1, num_2)
    elif operation == "*":
        return multiply(num_1, num_2)
    elif operation == "/":
        return divide(num_1, num_2)

print("Welcome to The Python Calculator!")
print(art.calculator)

should_continue = "n"

while True:
    if should_continue == "n":
        num_1 = float(input("Enter the first number: "))
        operation = input("+\n-\n*\n/\nPick an operation: ")
        num_2 = float(input("Enter the second number: "))
        result = calculate(num_1, num_2)

        print(f"{num_1} {operation} {num_2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    elif should_continue == "y":
        num_1 = result
        operation = input("+\n-\n*\n/\nPick an operation: ")
        num_2 = float(input("Enter the second number: "))
        result = calculate(num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
