import random
a = [random.randint(1,100) for i in range(5)]
print(a)
b = list(map(lambda x:x+10,a))
print(b)