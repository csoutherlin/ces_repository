#Create a function named age_in_days that takes an age in years (assume whole years only) and returns the age in days (ignore leap years). Assume each year has 365 days.
years = float(input("Enter your age: "))
days = (years * 365)
print(str(years )+ " years is equal to " + str(days ) + " days.")