monthly_income = int(input ("Enter your monthly income"))
total_monthly_expenses = int(input ("Enter your total monthly expenses"))

monthly_savings = monthly_income - total_monthly_expenses

#annual_interest_rate = 5%

projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(monthly_savings)
print(projected_savings)