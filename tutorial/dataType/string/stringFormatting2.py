# format 함수 사용

# 1. 숫자 바로 대입하기

exam1 = "I eat {0} apples".format(300)
print(exam1)

# 2. 문자열 바로 대입하기

exam2 = "I eat {0} apples".format("ten")
print(exam2)

# 3. 숫자 값을 가진 변수로 대입하기

number = 20
exam3 = "I eat {0} apples".format(number)
print(exam3)

# 4. 2개 이상의 값 넣기

number2 = 10
day = "three"

print("I ate {0} apples, so I was sick for {1} days.".format(number2, day))
print("I ate {0} apples, so I was sick for {0} days.".format(number2, day))

# 5. 이름으로 넣기

ment = "I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)
print(ment)

# 6. 인덱스와 이름을 혼용해서 넣기

hybrid = "I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)
print(hybrid)

# 7. 왼쪽, 오른쪽, 가운데 정렬
leftSort = "0{0:<10}0".format('left')
rightSort = "0{0:>10}0".format('right')
middleSort = "0{0:^10}0".format('middle')

print(leftSort)
print(rightSort)
print(middleSort)

# 8. 공백 채우기
leftSortFill = "0{0:<<10}0".format('left')
rightSortFill = "0{0:>>10}0".format('right')
middleSortFill = "0{0:^^10}0".format('middle')
print(leftSortFill)
print(rightSortFill)
print(middleSortFill)

# 9. 소수점 표현하기

y = 3.42134234
floatPrint = "{0:0.4f}".format(y)
floatPrint2 = "{0:10.4f}".format(y)

print(floatPrint)
print(floatPrint2)

# 10. '{' 또는 '}' 문자 표현하기
escape = "{{ and }}".format()
print(escape)

###########################################################
# f 문자열 포매팅 - 파이썬 3.6 버전 이상에서 사용하므로 넘어간다 #
###########################################################