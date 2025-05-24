import art

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
    "/": divide,
}
print("Welcome to The Python Calculator!")
print(art.calculator)

should_continue = "n"

while True:
    if should_continue == "n":
        num_1 = float(input("Enter the first number: "))
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        num_2 = float(input("Enter the second number: "))
        result = operations[operation](num_1, num_2)

        print(f"{num_1} {operation} {num_2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    elif should_continue == "y":
        num_1 = result
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        num_2 = float(input("Enter the second number: "))
        result = operations[operation](num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
