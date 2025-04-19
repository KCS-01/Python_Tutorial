# 딕셔너리

파이썬은 대응 관계를 나타낼 수 있는 딕셔너리(dictionary) 자료형이 있다.

`딕셔너리(dictionary)`는 `연관 배열(associative array)`, `해시(hash)`라고도 부른다.

## 정의

`사전`이라는 뜻을 가지고 있다. "city"이라는 단어에 "seoul"이라는 단어를 부합되게 하듯이 Key-Value를 한 쌍으로 가지는 자료형이다.

```
Key --> city
Value --> seoul
```

딕셔너리는 리스트, 튜플처럼 순서를 가지고 있지 않고, Key를 이용해서 Value 를 얻어낸다.

## 생성하기

```py
exam = { 'name': "char1ey", 'age': 31 }
```

## 딕셔너리 쌍 추가, 삭제하기

```py
a = {1: 'a'}
a[2] = 'b'

print(a) # {1: 'a', 2: 'b'}

del a[1]

print(a)

```

## Key를 이용해서 Value 얻기

```py
b = {'a': 10, 'b': 3, 3: 'c'}
print(b)
print(b['a'])
print(b['b'])
print(b[3])
# print(b[10])
```

없는 값을 부르려고하면 에러를 반환한다.

## 딕셔너리 생성시 주의사항

1. Key는 고유한 값이므로 중복되는 Key를 설정한다면, 나머지 값들이 무시된다.

```py
origin = {1: 'a', 1: 'b'}
print(origin) # {1: 'b'}
```

2. Key에 리스트를 사용할 수 없지만, 튜플은 사용할 수 있다.

Key에 리스트, 튜플이 문제가 아니라, 값이 변하는지 변하지 않는지에 달려있다

---

## 딕셔너리 관련 함수

1. Key 리스트 만들기 - keys

```py
a = {'name' : 'char1ey', 'age': 31}

keyList = a.keys()

print(keyList) # --> dict_keys(['name', 'age'])
```

dict_keys 객체를 리턴하게 되는데, 파이썬 3.0 이전에는 리스트를 반환했다.

리스트를 반환하게되면, 메모리의 낭비가 발생하는데, 이러한 메모리 낭비를 줄이기위해서 dict_keys 객체를 반환하도록 변경되었다.

dict_values, dict_items도 마찬가지로 3.0 이후에 추가된 것들이다.

리스트값이 필요하다면, 다음과 같이 사용할 수 있다.

```py
list(keyList)
```

dict 객체는 변환하지 않아도 기본적인 반복문에서 사용할 수 있다.

```py
for key in keyList:
    print(key)
```

dict 객체는 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.

2. Value 리스트 만들기 - values

```py
valueList = a.values()
```

3. Key, Value 쌍 얻기 - items

items 함수의 경우 Key, Value 쌍으로 `튜플`로 묶은 값을 dict_items 객체로 리턴한다.

```py
itemList = a.items()
# dict_items([('name', 'char1ey'), ('age', 31)])
```

4. Key: Value 쌍 모두 지우기 - Clear

```py
a.clear()
```

5. Key로 Value 얻기 - get

`a['name']`으로도 값을 뽑아낼 수 있지만 다음과 같이 get을 사용해도 된다.

위의 대괄호 표기법과 큰 차이점은 없는 값을 뽑으려고 할때, 에러대신에 None을 반환한다.

None은 '거짓'을 뜻한다.

```py
a.get('name')
a.get('phone')
```

다음과 같이 두번째 인자를 지정해주면, 값이 없을 경우 디폴트 값을 반환할 수 있다.

```py
a.get('phone', '010-1234-5678')
```

6. 해당 Key가 딕셔너리 안에 있는지 조사하기 - in

딕셔너리안에 있을 경우 `True`, 없을 경우 `False`를 반환한다.

```py
exam = {'name': 'char2ey', 'age': 31}

isName ='name' in exam
isEmail = 'email' in exam
```
