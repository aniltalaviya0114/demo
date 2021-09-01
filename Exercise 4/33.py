def decorators(p1,p2):
	def inner(func):

		return func(p1*p2)

	return inner
@decorators(5,2)  #f1 = 5*2 = 10

def multi(f1,f2=5): #10 + 5
	print(f1+f2)