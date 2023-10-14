#!/bin/python3

def newline():
	print('\n')
	

#Advanced Strings 4.50.20

my_name = "Chris"
print(my_name[0]) # first letter
print(my_name[-1]) # last letter

#Strings immutable - can cut n stuff

sentence = "This is a sentence"
print(sentence[:4]) #Grabbed 'This'
print(sentence.split()) #delimeter - default is space; so we grab first word even if we don't know it

sentence_split = sentence.split()
sentence_join=' '.join(sentence_split) # This is a sentence. Splits and rejoins!

quote = "He said 'give me all your money'"
print(quote) #print a quote with speech marks
quote = "He said \"Give me all your money\""
print(quote) #backslash character escaping


too_much_space = "                                     hi        "
print(too_much_space.strip()) #no space

print("A" in "Apple") #true
print("a" in "Apple") #false
letter = "A"
word = "Apple"
#if we search Apple for the letter A, the case matters. If it doesn't matter we can covert it to lowercase:
print(letter.lower() in word.lower()) #true && improved!

#5.01.00
#Instead of concat the string.. 
movie = "The Hangover"
print("My favourite movie is {}.".format(movie))#string format method
print("My favourite movie is %s." %movie) #%s method
print(F"My favourite movie is {movie}.") #string literal method - latest way
newline()



	#Dictionaries 			5.03.10 

#key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Espresso Martini": 8,} #drink = key, price = value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Chris", "Taylor"]}
print(employees)

employees['Legal'] = ["Mr. Day"] #adds new key:value pair
print(employees)
employees.update({"Sales":["Andy","Dwight"]})
print(employees) #adds new key:value pair

##update value
drinks['White Russian'] = 8
print(drinks)

#Get the value of key
print(drinks.get("White Russian")) #8



#5.09.35	Importing (new file, importing.py&)
