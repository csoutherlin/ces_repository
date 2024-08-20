#Create a function named celsius_to_fahrenheit that takes a temperature in Celsius and returns its equivalent in Fahrenheit. Use the formula:  F = C * 9/5 + 32.
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit ) + " degree Fahrenheit.")