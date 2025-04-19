exam = ['v', 'a', 'r']

print(id(exam))

a = [1, 2, 3]
b = a[:]

print(id(a)) # 139627523067008
print(id(b)) # 139627523067008

isSame = a is b # True
print(isSame)

a[0] = 4

print(a)
print(b)