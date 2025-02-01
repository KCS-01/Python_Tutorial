# 문자열 변경하기

# Pithon 문자열을 Python으로 변경

python = "Pithon"

# python[1] = "y"
# 오류발생, 문자열의 요소는 바꿀 수 있는 값이 아님
# 문자열은 변경 불가능한(immutable) 자료형이라고 함

# 슬라이싱을 활용하면 해결할 수 있다.
print(python[:1] + "y" + python[2:])