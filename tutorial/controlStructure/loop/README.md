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
