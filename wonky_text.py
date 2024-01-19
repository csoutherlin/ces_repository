#Create a function wonky_text that replaces every s with the $ sign, every e with the euro sign and every l with the £
def wonky_text():
    sentence = input("Please type a sentence: ")
    sentence = sentence.replace("s", "$").replace("e", "€").replace("l", "£")
    return sentence
   
print(wonky_text())