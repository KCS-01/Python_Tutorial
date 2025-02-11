# 반복문

## While 문

조건문이 참인 동안 While 문에 속한 문장들이 반복해서 수행된다.

1. 기본적인 While 문

```py
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if(treeHit == 10):
        print("나무 넘어갑니다.")
```

2. `break` - while 문 강제로 빠져나가기

`break`를 통해 반복문을 빠져나갈 수 있다

```py
# 남은 커피
coffee = 10

# 커피 가격
money = 300

while money:
    print("금액을 지불하여 커피를 판매합니다")
    coffee -= 1
    print("남은 커피는 %d 잔 입니다." % coffee)
    if coffee == 0:
        print("남은 커피가 없어 커피 판매를 중지합니다.")
        break
```

3. `continue` - while 문의 맨 처음으로 돌아가기

`continue`를 통해서 나머지가 0일 경우 print를 실행하지 않고, 처음으로 되돌아간다.

결과적으로 홀수만 찍게된다.

```py
a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
```

## For 문

```
for 변수  in `list` 혹은 `tuple` 혹은 `string`:
    수행할_문장1
    수행할_문장2
    ...
```

1. 일반적인 for 문

```py
test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)
```

2. 다양한 for 문

```py
a = [(1,2), (3,4), (5,6)]

for (first, last) in a:
    print(first + last)
```

3. for 문 응용

```py
# 점수가 60점 이상이면 합격, 아니면 불합격일때, 결과를 도출

score = [90, 25, 67, 45, 80]

for student in score:
    if student >= 60:
        print("합격")
    else:
        print("불합격")
```

4. for문 - continue

```py
# 60점 이상인 사람에게는 축하메시지 아닌 사람에게는 메시지 X

for student in score:
    if student < 60:
        continue
    print("%d 점 ㅊㅋㅊㅋ" % student)
```

5. for문 - range 함수

range 함수는 리스트를 자동으로 만들어준다.

for문과 같이 많이 사용된다.

```py
a = range(10)

print(a) # range(0, 10)
```

range는 0부터 10 미만의 숫자를 포함하는 range 객체를 만든다.

단, 끝 숫자는 포함되지 않는다.

```py
add = 0

for i in range(1, 11):
    add += i

print(add) # 55
```

```py
score = [90, 25, 67, 45, 80]

for number in range(len(score)):
    if score[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
```

6. **리스트 컴프리헨션(list comprehension)**

```
[표현식 for 항목 in 반복_가능한_객체 if 조건문]
```

파이썬에서는 리스트 안에 for 문을 포함할 수 있다.

이를 이용하여 좀 더 편리하고 직관적인 프로그래밍이 가능.

```py
a = [1, 2, 3, 4]

result = []

for num in a:
    result.append(num*3)

print(result) # [3, 6, 9, 12]
```

이를 리스트 컴프리헨션을 이용하면,

```py
a = [1, 2, 3, 4]

result = [num * 3 for num in a]

print(result) # [3, 6, 9, 12]
```

리스트 컴프리헨션 안에는 if 조건문도 사용할 수 있다.

```py
a = [1, 2, 3, 4]

result = [num * 3 for num in a if num % 2 == 0]

print(result) # [6, 12]
```

7. 이중 for 문

구구단을 구현해보자.

```py
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
```

이에 리스트 컴프리헨션을 적용하면,

```py
result = [x*y for x in range(2,10)
for y in range(1,10)]
```
