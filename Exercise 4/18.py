import random
a = [random.randint(0,1) for i in range(10)]

if sum(a) == 10:
    print("ALL")
elif 1 in a:
    print("ANY")
else:
    print("NONE")
print(a)



