import random
a = [random.randint(1,100) for i in range(25)]
a = sorted(a, reverse=False)
print(a)
