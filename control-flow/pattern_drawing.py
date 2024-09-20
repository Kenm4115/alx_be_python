
# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")

# Initialize the row counter
row = 0

# Outer loop for each row
while row < size:
    # Inner loop for each column in the row
    for col in range(size):
        print("*", end="")

    # Move to the next line after printing a row
    print()

    # Increment the row counter
    row += 1


"""
Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

Task Description:

Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

Instructions:

Prompt User for Pattern Size:

Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
Draw the Pattern:

First, use a while loop to iterate through each row of the pattern.
Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
After completing each row, print a newline character to move to the next row.
Continue until the pattern forms a square of the inputted size.

"""
