from functools import wraps

def debug(func):
	'''decorator for debugging passed function'''

	@wraps(func)
	def wrapper(*args, **kwargs):
		print("Full name of this method:", func.__qualname__)
		return func(*args, **kwargs)
	return wrapper

def debugmethods(cls):
	''' This is another decorator function, but this one is intended for classes.
     It takes a class cls as an argument. Inside this decorator,
      it iterates through the class attributes using vars(cls).items().
       If it finds any callable methods (functions), it replaces them with their
        debugged versions using setattr(cls, key, debug(val)).'''

	# check in class dictionary for any callable(method)
	# if exist, replace it with debugged version
	for key, val in vars(cls).items():
		if callable(val):
			setattr(cls, key, debug(val))
	return cls

# sample class
@debugmethods
class Calc:
	def add(self, x, y):
		return x+y
	def mul(self, x, y):
		return x*y
	def div(self, x, y):
		return x/y

mycal = Calc()
print(mycal.add(2, 3))
print(mycal.mul(5, 2))