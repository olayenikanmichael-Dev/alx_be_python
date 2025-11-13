# Prompt the user for the two numbers (stored as strings initially)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Try to convert both inputs to floats; if conversion fails, exit with a helpful message
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please enter valid numbers (integers or decimals).")
    raise SystemExit(1)

# Ask the user which operation to perform
operation = input("Choose the operation (+, -, *, /): ")

# Use match/case to choose and perform the operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose one of: +, -, *, /")
