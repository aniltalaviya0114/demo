class A:
    def first(self):
        print("hello")
    def second(self):
        print("second function")
class B(A):
    def therd(self):
        print("therd function called")

obj=B()
obj.therd()
obj.second()
obj.first()
