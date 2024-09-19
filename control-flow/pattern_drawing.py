
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
