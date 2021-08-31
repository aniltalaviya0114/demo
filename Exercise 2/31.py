l1 = [1,2,3,4,5]
l2 = [4,5,6,7]
l3 = l1

for i in l2:
    if i in l3:
        l3.remove(i)
    else:
        l3.append(i)
print(l3)
