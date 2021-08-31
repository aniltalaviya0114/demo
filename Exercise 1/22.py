class Emp:
    def __init__(self):
        print("Employee create")

    def __del__(self):
        print("Employee deleted")
obj = Emp()
del obj
