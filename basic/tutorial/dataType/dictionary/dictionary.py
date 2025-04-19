# 1. 생성하기

exam = { 'name': "char1ey", 'age': 31 }

print(exam)

# exam2 = {[ 1, 2]: 1, []: 2}

# print(exam2)

a = {1: 'a'}
a[2] = 'b'

print(a) # {1: 'a', 2: 'b'}

del a[1]

print(a)


b = {'a': 10, 'b': 3, 3: 'c'}
print(b)
print(b['a'])
print(b['b'])
print(b[3])
# print(b[10])


origin = {1: 'a', 1: 'b'}
print(origin) # b