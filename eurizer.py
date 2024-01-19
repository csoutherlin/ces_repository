def eurizer():
    sentence = input("Please type a sentence: ")
    sentence = sentence.replace("e", "€")
    return sentence
   
print(eurizer())