# 문자열 연산하기

# 1. 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 2. 문자열 곱하기
# 파이썬에서는 문자열에 곱을 하면 반복된다
a = "python "
print(a*2)

# 문자열 곱하기 응용
# 로그를 남기거나 디버깅할 때 활용할 수도 있다

log = "="*50
start = "Python Start"

print(log)
print(start)
print(log)

# 3. 문자열 길이 구하기
# len이라는 파이썬 기본 내장함수 사용

length = len(a)
print(length)

# 4. 문자열 인덱싱(indexing)과 슬라이싱(slicing)
example = "0123456789"

# print(example[0])
# print(example[1])
# print(example[2])
# print(example[3])
# print(example[-3])
# print(example[-2])
# print(example[-1])
# print(example[-0])

# 한 글자씩 뽑는것이 아닌 단어를 뽑고 싶다면
word = "Life is Good"

life = word[0:4]
life2 = word[:4]
life3 = word[:-8]
print(life)
print(life2)
print(life3)

# 문자열 나누기 활용
forecast = "20250202Snow"
date = forecast[:8]
weather = forecast[8:]
print(date)
print(weather)