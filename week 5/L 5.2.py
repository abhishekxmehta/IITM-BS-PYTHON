#key should be unique but duplication is allowed in value
d = {'key': 'value'}

d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d)
for key in d:
    print(key, d[key])


d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d.keys())
print(d.values())
print(d.items())
