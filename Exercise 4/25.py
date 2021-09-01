import string
import random
a = [random.choice(string.ascii_letters) for i in range(10)]
print(a)
print(' '.join(a))