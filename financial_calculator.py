# This is a program allows the user to access two different financial calculators: Investment and home loan calc

import math

print("""
Investment: to Calculate the amount of interest you'll earn on your investment
Bond: to calculate the amount you'll have to pay on a home loan
""")

cal_1 = str(input("""
Enter either 'Investment' or 'Bond' from the menu above to proceed:
""")).title()
#Calculate 'Investment' portion.
if cal_1 == 'Investment':
    # print ("Investment Calculator Selected")
    investment_amount = float(input("""
    Enter the amount of money that you are planning on depositing:"""))
    interest_rate = float(input("Interest rate:"))
    num_years = int(input("The number of years to invest:"))
    interest = input("Enter the type of interest 'Simple' or 'Compound':").title()

    # declare the interest rate into a percentage
    rate = interest_rate / 100

    # Calculation on the investment
    if interest == "Simple":
        total_amount = investment_amount * (1 + rate * num_years)
        print("R", round(total_amount, 2))
    elif interest == "Compound":
        total_amount = investment_amount * math.pow((1 + rate), num_years)
        # Print calculation
        print("R", round (total_amount, 2))
    else:
        print("Error: Please type in either 'simple' or 'compound'")
#Calclulate Bond option
elif cal_1 == "Bond":
    current_value = float(input("Enter the current value:"))
    interest_rate = float(input("Enter the annual interest rate:"))
    num_month = int(input("Enter the number of months you plan to take to repay the bond:"))

    monthly_rate = (interest_rate / 100) / 12

    repayment_amount = (monthly_rate * current_value) / (1 - (1 + monthly_rate) ** (-num_month))
    print(f"You will have to repay R{repayment_amount:.2f} on each month")
else:
    print("\nError: Invalid selection. Please enter either 'investment' or 'bond'.")


