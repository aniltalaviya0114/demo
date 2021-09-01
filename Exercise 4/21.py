import random
a = [random.randint(1,100) for i in range(10)]
print(a)
odd = filter(lambda x:x % 2!=0,a)
print("ODD Number :",list(odd))

even = filter(lambda x:x % 2==0,a)
print("EVEN Number :",list(even))
