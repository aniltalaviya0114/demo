import random
def generator(end):
    r = random.sample(range(end), 10)
    yield r

print(list(generator(100)))


