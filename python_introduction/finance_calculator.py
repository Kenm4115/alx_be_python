monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

# monthly savings
monthly_savings = monthly_income - monthly_expenses

# projected annual savings
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * interest_rate)

print(f'Your monthly savings: ${monthly_savings:.2f}')
print(f'Projected annual savings after including interest: ${
      projected_annual_savings:.2f}')


"""

Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

Task Description:

You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

Instructions:

User Input for Financial Details:

Prompt the user for their monthly income: “Enter your monthly income: ”.
Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
Calculate Monthly Savings:

Calculate the monthly savings by subtracting monthly expenses from the monthly income.
Project Annual Savings:

Assume a simple annual interest rate of 5%.
Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
Output Results:

Display the user’s monthly savings.
Display the projected annual savings after including interest.

"""
