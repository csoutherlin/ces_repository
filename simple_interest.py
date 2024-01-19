#Create a function named simple_interest that calculates simple interest. It should take three arguments: principal amount, rate of interest, and time in years. Use the formula: ( SI = P * R * T ). Return the calculated simple interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * (rate/100) * time)
print(simple_interest)