class Shoes:

	def __init__(self, name, price):
		self.name = name
		self.price = float(price)
		
	def budget_check(self, budget):
		if not isinstance(budget, (int, float)):
		#isinstance returns a boolean based on the type of variaable received; e.g. we want float/int type all other types will return false. 
			print("Invalid. Please enter a number.")
			exit()
			
	#change left over after shoes bought	
	def change(self, budget):
		return(budget - self.price)
		
	def buy(self, budget):
		self.budget_check(budget)
		
		if budget >= self.price:
			print(f'You can buy some {self.name}')
			
			if budget == self.price:
				print('You have exactly enough to buy')
			else:
				print(f"You can buy these shoes and have ${self.change(budget)} left over.")
			exit('Thanks for using the shoe budget app')
