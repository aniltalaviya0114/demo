l=list()
for i in range(1,11):
    l.append(i)
print(l)
m1 = map(lambda x:x**3,l)
print(list(m1))