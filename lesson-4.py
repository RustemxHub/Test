class Car:
	
	def __init__(self, model,pessenger, tyre):
		self.model = model
		self.pessenger = pessenger
		sels.tyre = tyre

	def move(self):
		return f'{self.model} - {self.pessenger} - {self.tyre}'

mersedes = Car('mersedes','5',5)
print(mersedes.move())

traktor = Car('traktor','2',3)
print(traktor.move())
		