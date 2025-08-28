def greater_than_10(num):
	return num > 10

def divide(a, b):
	if b == 0:
		raise ValueError
	return a / b


class Calculater:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self): 
		return self.num1 + self.num2
	
	def difference(self):
		return self.num1 - self.num2
	
	def divide(self):
		if self.num2 != 0:
			return self.num1 / self.num2
		raise ZeroDivisionError('Cannot divide by zero!!')
	
	def product(self):
		return self.num1 * self.num2
	