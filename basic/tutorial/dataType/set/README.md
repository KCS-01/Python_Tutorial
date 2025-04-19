# 집합(set)

집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다

## 집합 생성하기

```py
setArr = set([1, 2, 3])
print(setArr)
# {1, 2, 3}

setStr = set('hellooooo')
print(setStr)
# {'h', 'l', 'o', 'e'}

setTuple = set((1, 2, 3))
print(setTuple)
# {1, 2, 3}

setEmpty = set()
print(setEmpty)
# set()
```

## 집합 자료형의 특징

1. 중복을 허용하지 않는다.
2. 순서가 없다.
    - 순서가 없으므로 인덱싱을 통해서 값을 얻을 수 없다.
    - 만약, set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트, 튜플로 변환해야한다.

```py
setToList = list(setStr)
print(setToList)

setToTuple = tuple(setStr)
print(setToTuple)
```

## 교집합, 합집합, 차집합 구하기

set은 집합을 활용할 때 유용하다

1. 교집합

```py
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

intersection1 = a & b
print(intersection1)
# {3, 4, 5}

intersection2 = a.intersection(b)
print(intersection2)
# {3, 4, 5}
```

2. 합집합

```py
c = set([1,2,3,4,5])
d = set([5,6,7,8,8])

union1 = c | d
print(union1)
# {1, 2, 3, 4, 5, 6, 7, 8}

union2 = c.union(d)
print(union2)
# {1, 2, 3, 4, 5, 6, 7, 8}
```

3. 차집합

```py
e = set(['a', 'b', 'c', 'd', 'e'])
f = set(['b', 'c', 'd', 'g'])

difference1 = e - f
print(difference1)
# {'e', 'a'}

difference2 = f - e
print(difference2)
# {'g'}

difference3 = f.difference(e)
print(difference3)
# {'g'}

difference4 = e.difference(f)
print(difference4)
# {'e', 'a'}
```

---

## 집합 자료형 관련 함수

1. 값 1개 추가하기 - add

```py
setAdd = set([1, 2, 3])
print(setAdd)
# {1, 2, 3}

setAdd.add(4)
print(setAdd)
# {1, 2, 3, 4}
```

2. 값 여러개 추가하기 - update

```py
setUpdate = set([1, 2, 3])
print(setUpdate)
# {1, 2, 3}

setUpdate.update([4, 5, 6])
print(setUpdate)
# {1, 2, 3, 4, 5, 6}
```

3. 특정 값 제거하기 - remove

```py
setRemove = set([1, 2, 3])
print(setRemove)
# {1, 2, 3}

setRemove.remove(2)
print(setRemove)
# {1, 3}
```
