#!/bin.python3

from shoes import Shoes

low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s', 120)
high = Shoes('Off Whites', 400)

try:
	shoe_budget = float(input('Input your shoe budget: '))
except ValueError:
	exit('Please enter a number')
	
for shoes in [high, medium, low]: #need to highest to lowest
	shoes.buy(shoe_budget) #in shoes class
	

#6.22.30 Five stages of ethical hacking
