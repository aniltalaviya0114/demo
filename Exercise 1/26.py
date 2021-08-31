class my_parent_class:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y

    def sub(self):
        return self.x-self.y

    def print_result(self):
        print(self.x + self.y)
        print(self.x - self.y)

obj = my_parent_class(2,3)
obj.print_result()
