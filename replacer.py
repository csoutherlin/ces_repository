def replacer():
    sentence = input("Please type a sentence: ")
    sentence = sentence.replace("s", "$").replace("e", "€")
    return sentence
   
print(replacer())
