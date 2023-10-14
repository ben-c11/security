# 5.42.00 	Accepting user input

#!/bin/python3

#name = input("Enter your name: ")
#drink = input(f"Hi {name}, what's your favourite drink? ")
#print(f"Hello, {name}. Have a {drink.lower()}")

#Calculator input 5.44.30

x = float(input("Give me a number: ")) #Can replace float for int but need the decimal points!
o = input("Give me an operator: ")
y = float(input("Give me another number: "))

if o == "+":
	print(x+y)
elif o == "-":
	print(x-y)
elif o == "/":
	print(x/y)
elif o == "*":
	print(x*y)
elif o == "**" or o == "^2":
	print(x**y)
else:
	print("Unkown operator.")


