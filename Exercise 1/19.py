def fun(*args):
   if len(args) == 2:
       print(args[0] * args[1])
   elif len(args) == 3:
       print(args[0],args[1],args[2])
   elif len(args) == 4:
       print(args[0]+args[1]+args[2]+args[3])
   elif len(args)==5:
       print((args[0]*args[1])+(args[2]*args[3]*args[4]))
   elif len(args) <2:
       print("Enter 2 or more then 2")

fun(2,3,4,5,6)

