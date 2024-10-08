
def safe_divide(numerator, denominator):
    """Perform safe division, handling division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform the division
        result = num / denom
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

# Uncomment for testing the function directly
# if __name__ == "__main__":
#     print(safe_divide(10, 2))  # Expected: 5.0
#     print(safe_divide(10, 0))  # Expected: Division by zero error
#     print(safe_divide(10, 'a'))  # Expected: Non-numeric input error


"""
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

robust_division_calculator.py:
Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.
main.py for Command Line Interaction:
This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.

Expected Behavior:
The script is executed from the command line with two additional arguments representing the numerator and denominator. Here are sample commands and the expected outputs:

Normal Division:
  python main.py 10 5
Expected Output: The result of the division is 2.0

Division by Zero:
  python main.py 10 0
Expected Output: Error: Cannot divide by zero.

Invalid Input (Non-numeric):
  python main.py ten 5
Expected Output: Error: Please enter numeric values only.

Implementation Notes for you:
Focus on error handling within safe_divide in robust_division_calculator.py. Ensure you cover the scenarios detailed above.
Test your function using main.py by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.
This task helps you practice writing error-resistant code, a crucial skill in software development.

"""
