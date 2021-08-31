a = int(input("Enter 1 Value :"))
b = int(input("Enter 2 Value :"))
c = int(input("Enter 3 Value :"))

if a > b and a > c:
    print("A number is big",a)
elif b > a and b > c:
    print("B number is big",b)
else:
    print("C number is big",c)

print(max(a,b,c))
print(min(a,b,c))