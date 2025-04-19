# 파이썬 함수 구조

```py
def function_name(__parameter):
    # 수행 문장 1
    # 수행 문장 2
    # ...
```

## 매개변수 지정 호출

다음과 같이 순서에 상관없이 사용할 수 있음

```py
def sub(a, b):
    return a - b

result1 = sub(a = 7, b = 3)
result2 = sub(b = 3, a = 7)

print(result1)  # 4
print(result2) # 4
```

## 입력값이 몇 개인지 모를경우

일반적인 함수 형태에서 매개변수 앞에 `*`를 붙여사용

```py
def function_name(*__parameter):
    # 수행할 문장
```

### 예시

```py
def add_many(*arguments):
    result = 0
    for i in arguments:
        result = result + i
    return result

result = add_many(1,2,3,4,5)
print(result) # 15

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result) # 55
```

## 키워드 매개변수(keyword arguments, kwargs)

키워드 매개변수를 사용할 경우, 매개변수 앞에 `**`를 붙여서 사용

입력받은 매개변수를 딕셔너리가 되고 모든 `Key = Value` 형태의 입력값이 그 딕셔너리에 저장됨

```py
def print_keyword_arguments(**keyword_arguments):
    print(keyword_arguments)

print_keyword_arguments(a = 1, b = 'seconds', third = 3)
# {'a': 1, 'b': 'seconds', 'third': 3}
```

## 함수 내부에서 함수 밖의 변수를 변경하는 방법

1. return 사용

```py
a = 1

def global_variable(param):
    a = a + 1
    return a

print(a) # 1

a = global_variable(a)
print(a) # 2
```

2. global 명령어 사용

```py
a = 1

def global_variable():
    global a
    a = a + 10

global_variable()

print(a)
```

3. lambda 예약어

lambda는 def와 동일한 역할을 하며,

보통 함수를 한 줄로 간결하게 만들 때 사용

- def를 사용할 정도로 복잡하지 않을 경우 사용
- def를 사용할 수 없을 경우에 사용

lambda 문법

```py
# 함수명 = lambda 매개변수_1, 매개변수_2, ... : 매개변수를 이용한 표현식
function_name = lambda param_1, param_2, param_3 : param_1 + param_2 - param_3

# return 명령어가 없더라도, 표현식의 결과값을 리턴
result = function_name(1, 2, 3)
print(result) # 0
```
