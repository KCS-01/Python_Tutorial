# if문

파이썬의 if문의 기본 구조는 다음과 같다.

```py
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장...
else:
    수행할 문장A
    수행할 문장B
    수행할 문장...
```

if 문에 속하는 모든 문장에 들여쓰기를 해야한다.

들여쓰기를 하지 않으면 오류가 발생한다.

```py
if 조건문:
    수행할 문장1
수행할 문장2 # 들여쓰기 하지 않으면 에러가 발생한다.
    수행할 문장...
else:
    수행할 문장A
    수행할 문장B
    수행할 문장...
```

# and, or, not

파이썬의 조건을 판단하는 연산자는 >, <, >= 등 말고도 and or not이 있다.

- x or y : x와 y 둘 중 하나만 참이어도 참
- x and y : x와 y 모두 참이어야 참
- not x : x가 거짓이면 참

## or

```py
money = 2000
card =True

if money >= 3000 or card:
    print("택시를 타고 가자")
else:
    print("걸어가자")
```

## in ,not in

### in

```py
list = ['l', 'i', 's', 't']
tuple = ('t', 'u', 'p', 'l', 'e')
string = 'string'

isInList = 'i' in list
isInTuple = 'y' in tuple
isInString = 't' in string

print(isInList) # True
print(isInTuple) # False
print(isInString) # True
```

### not in

```py
list = ['l', 'i', 's', 't']
tuple = ('t', 'u', 'p', 'l', 'e')
string = 'string'

isInList = 'i' not in list
isInTuple = 'y' not in tuple
isInString = 't' not in string

print(isInList) # False
print(isInTuple) # True
print(isInString) # False
```

# pass

조건문에 따라서 아무일도 안하고 넘어가고 싶을경우에는 `pass`를 사용한다.

```py
pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')
```

# elif

다양한 조건을 판단하기 위해서는 `elif`를 사용한다.

```
주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
```

```py
pockey = ['cellphone', 'coin']
card = False

if 'money' in pockey:
    print('택시를 타고 간다')
else:
    if card:
        print("택시를 타고 간다")
    else:
        print("걸어 간다")
```

위 처럼 다중 if문을 통해서 구현할 수 있지만,

elif를 사용하면 좀더 depth를 줄일 수 있다.

```py
pockey = ['cellphone', 'coin']
card = False

if 'money' in pockey:
    print('택시를 타고 간다')
elif card:
    print("택시를 타고 간다")
else:
    print("걸어 간다")
```

# if문을 한 줄로 작성하기

```py
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
```

위와 같이 두줄로 작성되어 있을 때 한 줄로 변경하면

```py
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
```

if 문 다음에 수행할 문장을 콜론(:) 뒤에 바로 적었고, else문 또한 같은 원리다.

# 조건부 표현식

```py
# score가 60 이상일 경우 message에 문자열 'success',
# 아닐 경우에는 문자열 'failure'를 대입하라

if score >= 60:
    message = "success"
else:
    message = "failure"
```

위의 조건문을 파이썬의 조건부 표현식을 이용하면 다음과 같이 나타낼 수 있다.

```py
# 변수 = 조건문이_참인_경우_값 if 조건문 else 조건문이_거짓인_경우의_값
message = "success" if score >= 60 else "failure"
```

조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
