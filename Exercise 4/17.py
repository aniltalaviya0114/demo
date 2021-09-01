class Whether:
    a = 123
#print(hasattr(Whether,'a'))
if hasattr(Whether,'a') == True:
    print("YES")
else:
    print("NO")

print(getattr(Whether,'a'))
setattr(Whether,'a','Anil')
print(getattr(Whether,'a'))
delattr(Whether,'a')
print(getattr(Whether,'a'))
#print(delattr(Whether,'a'))