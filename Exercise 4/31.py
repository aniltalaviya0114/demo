# Create a decorator that adds two random values between 1 to 10 to the functions
# where this decorator is used. Create 4 functions add, sub, mul, div which will have
# this decorator and call the 4 functions. When you’re calling the function you
# should not pass any parameter however all the functions will be defined with
# parameters.

import random

def dec_func(func1):
    def inner_func():
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        print("x :", x, "y :", y)
        return func1(x, y)

    return inner_func


@dec_func
def add(x, y):
    return x + y


@dec_func
def sub(x, y):
    return x - y


@dec_func
def mul(x, y):
    return x * y


@dec_func
def div(x, y):
    return x / y


print("Addition :", add())
print("Subtraction :", sub())
print("Multiplication :", mul())
print("Division :", div())


