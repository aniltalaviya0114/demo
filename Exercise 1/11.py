var = input("Enter three number of , :")
var1 = var.split(",")

a = var1[0]
b = var1[1]
c = var1[2]

if a > b and a > c:
    print("A number is big",a)
elif b > a and b > c:
    print("B number is big",b)
else:
    print("C number is big",c)

print(max(a,b,c))
print(min(a,b,c))