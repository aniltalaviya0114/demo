a = {'A': {'B': {'C': {'D': [100, 200, 300], 'E': {40, 50, 60}}, 'F': 80, 'G': 90}}}
print(a['A'])
print(a['A']['B'])
print(a['A']['B']['C'])
print(a['A']['B']['C']['D'])
print(a['A']['B']['C']['E'])

print(a['A']['B']['C']['E'].pop())