class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company

	def __str__(self):
		return f"My name is {self.name} and I work in {self.company}."


my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)