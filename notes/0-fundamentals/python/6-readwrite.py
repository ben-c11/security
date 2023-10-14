#!/bin/python3

#open command reads and writes files

months = open('6-months.txt')
print(months)
print(months.mode) #print r for readable
print(months.readable()) #boolean, true
#print(months.read()) #actually reads our file
#print(months.readline()) #reads just one line at a time (if file already read, prints space!) 
#print(months.readlines()) #prints array of the file
#months.seek(0) #go back to first month
#print(months.readlines()) #printing twice gives an empty array; this is because file has already been read, similar to that above. Instead we can use seek() which returns us to the start so we can read it again

#Can also use a for loop to iterate through:
for month in months:
	print(month.strip()) #strip gets rid of extra spaces

months.close #must close out of it
#<_io.TextIOWrapper name='6-months.txt' mode='r' encoding='UTF-8'>
# name of file, mode = reading, encoding UTF-8; we can check the mode of the file (see above)



# 5.57.20 	Writing to a file

days = open('days.txt', 'w') #open a new file, days.txt and set to write mode
print(days.mode) #w (for write mode)
print(days) #<_io.TextIOWrapper name='days.txt' mode='w' encoding='UTF-8'>
days.write("Monday") #cat days.txt == Monday
days.write("\nTuesday") #overwrites Monday.
# to append:
days = open('days.txt', "a") #change to 'a'
days.write('\nWednesday') #Tuesday Wednesday when cat 


days.close()



#Next up Classes and Objects 6.00.20
