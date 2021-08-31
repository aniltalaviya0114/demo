print("-----------------------MULTIPLE-------------------------------")
class A:
    def show(self):
        print("First Class")
class B(A):
    def show(self):
        print("Second Class")
        #super().show()
class C(A):
    def show(self):
        print("Thered Class")
        #super().show()
class D(B,C):
    pass
obj = D()
obj.show()


print("-----------------------MULTI-LEVEL-------------------------------")
class Animal:
    def speak(self):
        print("Animal Speaking")

class Cat(Animal):
    def smile(self):
        print("Cat Smilling")
obj = Cat()
obj.speak()
obj.smile()

