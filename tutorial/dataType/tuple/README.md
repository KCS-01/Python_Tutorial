# 튜플

## 1. 튜플 생성하기

```py

tuple01 = ()

tuple02 = (1, )

tuple03 = (1, 2, 3)

tuple04 = 1, 2, 3

tuple05 = ('a', 'b', ('ad', 'bd'))

```

위와 같이 튜플을 생성할 수 있다.

리스트와 다른점은

1. 한개의 요소만을 가질 경우 쉼표(,)를 붙여야 한다.
2. 1, 2, 3 처럼 소괄호를 생략할 수 있다.

## 튜플과 리스트의 차이

1. 리스트는 값을 변경할 수 있으나, 튜플은 요솟값을 변경할 수 없다.
    - 프로그램 실행중 요솟값을 변경하고 싶지 않다면(=상수) 튜플을 사용한다.
    - 보통은 값을 변경하는 경우가 많아, 튜플보다 리스트를 많이 사용한다.

## 튜플의 요솟값 변경한다면

```py
# 삭제시
examDel = (1, 2, 'a', 'b')
del examDel[0]

# Traceback (most recent call last):
#   File "/home/char1ey/char1ey/python_study/tutorial/dataType/tuple/tuple.py", line 12, in <module>
#     del exam[0]
# TypeError: 'tuple' object doesn't support item deletion

examModify = (1, 2, 'a', 'b')
examModify[1] = 'c'

# Traceback (most recent call last):
#   File "/home/char1ey/char1ey/python_study/tutorial/dataType/tuple/tuple.py", line 15, in <module>
#     examModify[1] = 'c'
# TypeError: 'tuple' object does not support item assignment
```

## 튜플 다루기

```py
exam = (1, 2, 3, 4, 5)

# 1. 인덱싱

indexing = exam[2]
print(indexing)
# 2. 슬라이싱

slicing = exam[1:3]
print(slicing)
# 3. 튜플 더하기

plus = exam + (6, 7)
print(plus)
# 4. 튜플 곱하기

multiply = exam * 3
print(multiply)
# 5. 튜플 길이 구하기

length = len(exam)
print(length)
```
