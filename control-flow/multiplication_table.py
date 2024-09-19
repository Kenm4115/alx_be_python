
# Prompt the user for a number

number = int(input("Enter a number to see its multiplication table: "))
x = number

# Generate and print the multiplication table

for y in range(1, 11):
    z = x * y
    print(f"{x} * {y} = {z}")
