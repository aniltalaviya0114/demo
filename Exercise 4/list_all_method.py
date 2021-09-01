l1 = [10,2,3,4,5,6,7,8,9,1]
print(l1)


l1.sort()
print("Sort Method :",l1)

l1.pop(2)
print("POP Method :",l1)

l1.insert(2,11)
print("Insert Method :",l1)

l5 = l1.index(5)
print("Index Method :",l5)

l4 = [11,12,13,14,15]
l1.extend(l4)
print("Extend Method :",l1)

l1.reverse()
print("Reverse Method :",l1)

l1.append(11)
print("Append Method :",l1)

l1.remove(11)
print("Remove Method :",l1)

l3 = l1.count(2)
print("Count Method :",l3)

l2 = l1.copy()
print("Copy Method :",l2)

l2.clear()
print("Clear Method :",l2)

for i in range(5):
    print(i,)
