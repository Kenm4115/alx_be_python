
# explore_datetime

from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)


def calculate_future_date(days):
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)


if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer.")


"""

Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

Task Instructions:
Your task is to create a Python script named explore_datetime.py. This script will demonstrate your ability to use the datetime module for handling dates and times in Python.

Part 1: Display the Current Date and Time

Research how to use the datetime module to obtain the current date and time.
Create a function with a name display_current_datetime and
save the current date inside a current_date variable
Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
Part 2: Calculate a Future Date

Prompt the user to enter a number of days (as an integer).
Create a function with a name calculate_future_date and
saves the future date inside a future_date variable
Calculate what the date will be after adding the specified number of days to the current date.
Print the future date in a format like “YYYY-MM-DD”.
Guidance:
Start by importing the necessary components from the datetime module.
Look into the datetime.now() function to get the current date and time.
Use timedelta(days=number_of_days) to represent the duration to add to the current date.
Remember, Python’s official documentation is an excellent resource for learning how to use the standard library modules.

"""
