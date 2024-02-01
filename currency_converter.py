transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21]

transactions_usd = []

#for transaction in transactions_aed: 
#    item_usd = transaction * 0.27
#    transactions_usd.append(item_usd)
#print(transactions_usd)

i = 0
while i <= len(transactions_aed) -1:
    item_usd = transactions_aed[i] * 0.27
    print("Converting value", transactions_aed[i])
    transactions_usd.append(item_usd)
    i += 1








#lst = [2, 4, 5, 6]

#for number in lst:
#    if number % 2 == 0:
#        print(number * 2)


