x=(1,2,3,4,5)
y=(4,5,6,7)
z=[]
for i in x:
    if i not in y:
        z.append(i)
for j in y:
    if j not in z:
        z.append(j)
z=tuple(z)
print(z)