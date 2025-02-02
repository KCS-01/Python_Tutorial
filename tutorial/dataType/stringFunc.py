# 문자열 관련 함수

string = "   char1ey   "

# 1. 원하는 문자열 갯수 세기 - count

coutnA = string.count('a')
print(coutnA)

# 2. 위치 알려 주기 - find, index

findE = string.find('e')
print(findE)
print(string[findE])

findQ = string.find('q')
print('없을 경우에는 -1을 반환한다 ::', findQ)

index1 = string.index('1')
print(index1)

# 다음과 같이 없는 문자열을 찾을때는 오류가 발생한다
# indexQ = string.index('Q')
# print(indexQ)

# 3. 문자열 삽입 - join
# 문자열뿐만 아니라 리스트, 튜플에서도 사용한다

joinRest = ",".join(string)
print(joinRest)

# 4. 소문자를 대문자로 바꾸기 - upper
upperCase = string.upper()
print(upperCase)

# 5. 대문자를 소문자로 바꾸기 - lower
lowerCase = upperCase.lower()
print(lowerCase)

# 6. 왼쪽 공백 지우기 - lstrip
trimLeft = string.lstrip()
print(trimLeft)

# 7. 오른쪽 공백 지우기 - rstrip
trimRight = string.rstrip()
print(trimRight)

# 8. 양쪽 공백 지우기 - strip
trimSide = string.strip()
print(trimSide)

# 9. 문자열 바꾸기 - replace
replace = string.replace('char', 'varchar')
print(replace)
print(string)

# 10. 문자열 나누기 - split

split = string.split('1')
print(split)