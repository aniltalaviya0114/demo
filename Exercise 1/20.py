class A:


    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def show(self):
        print(self.a + self.b)


obj = A(2,3)
obj.show()