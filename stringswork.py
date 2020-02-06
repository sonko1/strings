#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#Use the format() method to insert numbers into strings:
a = "Hello"
b = "World"
print("hi {}".format(b))
print('h' in a)
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
#Built-in string function/Methods
n="HELLO"
a="hello world"
b=a.capitalize()
#Upper case the first letter in this sentence:
print(a.capitalize())
#The upper() method returns the string in upper case:
print(a.upper())
#The the output remains the same
print(b)
#The lower() method returns the string in lower case:
print(n.lower())
#Python String center() Method
txt = "Gabriel"

x = txt.center(20)

print(x)
#Python String count() Method
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
#Python String endswith() Method
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
#Python String index() Method
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)




