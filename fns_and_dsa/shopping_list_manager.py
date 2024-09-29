
# shopping_list_manager

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f'"{item}" has been added to the shopping list.')

        elif choice == '2':
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the shopping list.')
            else:
                print(f'"{item}" not found in the shopping list.')

        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


"""

Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

Task Description:
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list.
Implement functionality to add items to the list, remove items, and display the current list.
User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.

"""
