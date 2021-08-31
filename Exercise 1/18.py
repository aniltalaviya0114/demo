def f1():
    print("Called by f1()")
def f2():
    f1()
    print("Called by f2()")
f2()