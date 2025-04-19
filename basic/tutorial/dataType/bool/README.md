# 불

참, 거짓을 나타내는 자료형이다.

-   True
-   False

True, False는 파이썬의 예약어로 true, false와 같이 작성하면 안되고 항상 첫 문자를 대문자로 작성해야한다.

## 사용하기

```py
a = True
typeTrue = type(a)
print(typeTrue) # <class 'bool'>

b = False
typeFalse = type(b)
print(typeFalse) # <class 'bool'>
```

-   조건문의 리턴값으로도 사용한다

```py
print(1 == 1)
```

## 자료형의 참과 거짓(Truthy와 Falsy)

```py
print(bool("python")) # True

print(bool("")) # False

print(bool([1, 2, 3])) # True

print(bool([])) # False

print(bool((1, 2, 3))) # True

print(bool(())) # False

print(bool({'a': 1})) # True

print(bool({})) # False

print(bool(1)) # True

print(bool(0)) # False

print(bool(None)) # False

```

## 자료형의 참과 거짓을 프로그램에서 사용하는 예시

```py
a = [1, 2, 3, 4]

while a:
    print(a.pop())
```

```
while 조건문:
    수행할 문장
```
