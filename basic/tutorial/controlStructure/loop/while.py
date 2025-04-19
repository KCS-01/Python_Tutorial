# 열번 찍어 안 넘어가는 나무 없다

treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if(treeHit == 10):
        print("나무 넘어갑니다.")

# While문 강제로 빠져나가기

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

# while 문의 맨 처음으로 돌아가기

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)