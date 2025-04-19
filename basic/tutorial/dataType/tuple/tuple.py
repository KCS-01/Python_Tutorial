# 튜플(tuple)

# ※.튜플은 리스트와 거의 비슷하나, 다른점이 있다.
# 리스트는 대괄호 [], 튜플은 소괄호 ()
# 리스트는 요솟값의 생성, 삭제, 수정이 가능한 반면에, 튜플은 요솟값을 바꿀 수 있다.

###################################################

# 1. 튜플 생성하기

# exam = (1, 2, 'a', 'b')
# del exam[0]

# examModify = (1, 2, 'a', 'b')
# examModify[1] = 'c'

###################################################

exam = (1,2,3,4,5)

# 1. 인덱싱

indexing = exam[2]
print(indexing)

# 2. 슬라이싱

slicing = exam[1:3]
print(slicing)
# 3. 튜플 더하기

plus = exam + (6, 7)
print(plus)
# 4. 튜플 곱하기

multiply = exam * 3
print(multiply)
# 5. 튜플 길이 구하기

length = len(exam)
print(length)