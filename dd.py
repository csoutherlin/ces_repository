string = "Python"
print(string[0])
print(string[2])
print(string[-1])
print(string[1:4]) #slicing
print(string[3:])
print(string[:3])
print(string[::2])
print(string[-2::-1])
string1 = "apple"
string2 = "orange"
print(string1 == string2) #true or false (compare strings)
print("a" > "b") #b has higher ASCII code
print("abc" < "acad")
print('C' in 'Code')
print('c' in 'Code')
print('mail' in 'gmail')
date_str = "12/11/1975"
day, month, year = date_str.split("/")
print(day)

upper_cased = string.upper()
print(upper_cased)

string2 = "I have a cat"
new_string = string2.replace("cat", "dog")
print(new_string)

text = "hello everyone in the world"
print(text.find("world"))
print(text.find("l", 4))