# class A:
#     def __init__(self,i):
#         self.i = i
# class B(A):
#     def __init__(self):
#         A.__init__(self,5)
#
# print(issubclass(B,A))

class A:
    pass
class B(A):
    pass
print(issubclass(B,A))
