principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time in years: "))

interest = principal_amount * annual_interest_rate * time / 100

print("The simple interest is: " + str(interest))
