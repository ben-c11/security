#!/bin/python3

from Employees import Employees

#Create Employee objects using the Employee class
e1 = Employees("Bob", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Linda", "Executive", "CIO", 150000, 10)

print(e1.name) #Bob
print(e2.role) #CIO

print(e1.eligible_for_retirement())

#6.08.00 - Shoe budget
