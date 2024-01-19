def dollarizer():
    sentence = input("Please type a sentence: ")
    sentence = sentence.replace("s", "$")
    return sentence
   
print(dollarizer())