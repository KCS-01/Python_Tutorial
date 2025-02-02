# set 자료형

setArr = set([1, 2, 3])
print(setArr)

setStr = set('hellooooo')
print(setStr)

setTuple = set((1, 2, 3))
print(setTuple)

setEmpty = set()
print(setEmpty)


setToList = list(setStr)
print(setToList)

setToTuple = tuple(setStr)
print(setToTuple)


a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

intersection1 = a & b
print(intersection1)

intersection2 = a.intersection(b)
print(intersection2)

c = set([1,2,3,4,5])
d = set([5,6,7,8,8])

union1 = c | d
print(union1)

union2 = c.union(d)
print(union2)


e = set(['a', 'b', 'c', 'd', 'e'])
f = set(['b', 'c', 'd', 'g'])

difference1 = e - f
print(difference1)

difference2 = f - e
print(difference2)

difference3 = f.difference(e)
print(difference3)

difference4 = e.difference(f)
print(difference4)