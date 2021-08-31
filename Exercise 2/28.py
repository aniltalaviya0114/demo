# keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#
# myDict = { k:v for (k,v) in zip(keys, value)}
# print(myDict)
c = 1
d1 = {}
for i in range(97,123):
    d1[chr(i)]=c
    c=c+1
print(d1)

