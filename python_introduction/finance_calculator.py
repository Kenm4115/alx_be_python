monthly_income = float(input ("Enter your monthly income"))
monthly_expenses = float(input ("Enter your total monthly expenses"))

#monthly savings
monthly_savings = monthly_income - monthly_expenses

#projected annual savings
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * interest_rate)

print(monthly_savings)
print(projected_annual_savings)