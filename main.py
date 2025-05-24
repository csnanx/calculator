def add(num_1, num_2):
    return num_1 + num_2
def subtract(num_1, num_2):
    return num_1 - num_1
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

num_1 = float(input("Enter the first number: "))
operation = input("+\n-\n*\n/\nPick an operation: ")
num_2 = float(input("Enter the second number:"))
print(f"{num_1} {operation} {num_2} = {calculate(num_1, num_2)}")