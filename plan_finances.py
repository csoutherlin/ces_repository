#Write a function named plan_finances that takes a principal amount, rate of interest, time in years, and a desired final amount after simple interest. The function should return whether the final amount after simple interest is achieved from the principal within the given time and rate.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
downpayment = float(input("Enter the downpayment: "))
plan_finances = ((principal-downpayment) * (rate/100) * time)
print(plan_finances)