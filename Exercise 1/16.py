def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
num = int(input("Enter the Number :"))

if num < 0:
    print("Does not exit negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("factorial of", num, "is :",factorial(num))