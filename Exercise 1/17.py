def cal(n):
    if n == 1:
        def add(num1, num2, num3):
            return num1 + num2 + num3
        print(add(int(input("Enter 1 number :")),int(input("Enter 2 number :")),int(input("Enter 3 number :"))))
    elif n == 2:
        def sub(num1, num2, num3):
            return num1 - num2 - num3
        print(sub(int(input("Enter 1 number :")), int(input("Enter 2 number :")),int(input("Enter 3 number :"))))

    elif n == 3:
        def multi(num1, num2, num3):
            return num1 * num2 * num3
        print(multi(int(input("Enter 1 number :")), int(input("Enter 2 number :")),int(input("Enter 3 number :"))))

    elif n == 4:
        def division(num1, num2):
            return num1 / num2
        print(division(int(input("Enter 1 number :")), int(input("Enter 2 number :"))))

    elif n == 5:
        def exponent(num1, num2):
            return num1 ** num2
        print(exponent(int(input("Enter 1 number :")), int(input("Enter 2 number :"))))

    elif n == 6:
        def flordivision(num1, num2):
            return num1 // num2
        print(flordivision(int(input("Enter 1 number :")), int(input("Enter 2 number :"))))

    else:
        print("Invalid number")
cal(int(input("plase enter number :")))