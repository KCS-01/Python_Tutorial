## 따옴표 포함 시키기

# 1. 문자열에 작은 따옴표 포함시키기
# Python's favorite food is perl

# 아래의 경우 정상적으로 출력된다
food = "Python's favorite food is perl"
print(food)

# 아래의 경우 정상적으로 출력되지 않는다. Python이 문자열로 인식된다
# food = 'Python's favorite food is perl
# print(food)

# 2. 문자열에 큰 따옴표를 포함시키기
# "Python is very easy." he says.

say  = '"Python is very easy." he says.'
print(say)

# 3. 역슬래시(\) 사용
food2 = 'Python\'s favorite food is perl'
say2  = "\"Python is very easy.\" he says."

## 줄바꾸기

# 1. 줄바꿈(\n) 이스케이프
# Life is too short
# You need python

# 단점: 읽기가 불편하다

multiLine = "Life is too short\nYou need python"
print(multiLine)

# 2. 연속된 작은 따옴표 3개 또는 큰따옴표 3개 사용하기

multiLine2 = '''
Life is too short
You need python
'''
print(multiLine2)

multiLine3 = """
Life is too short
You need python
"""
print(multiLine3)