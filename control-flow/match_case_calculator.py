
# Prompt for user input

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
value = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match-case

match value:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Error: Invalid operation. Please choose +, -, *, or /.")
