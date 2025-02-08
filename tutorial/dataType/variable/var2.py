from copy  import copy

a = [1, 2, 3]
b = copy(a)

print(id(a))
print(id(b))