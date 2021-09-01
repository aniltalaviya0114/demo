def decor1(func):
    def inner():
        x = func()
        return x ** 2
    return inner

def decor(func):
    def inner():
        x = func()
        return x + 10
    return inner
@decor
@decor1
def num():
    return 5

print(num())