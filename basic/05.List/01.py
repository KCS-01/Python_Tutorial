# 빈 리스트 생성
# animals = []

# 리스트 생성
animals = ["사자", "호랑이", "고양이", "강아지"]

# 리스트 접근
lion = animals[0]
tiger = animals[1]
cat = animals[2]
puppy = animals[3]

# 리스트 추가
snake = "뱀"
animals.append(snake)

# 리스트 삭제
del animals[0]

# 리스트 슬라이싱
newList = animals[1:2]

# 리스트 길이
length = len(animals)

# 리스트 정렬
animals.sort()
animals.sort(reverse=True)
print(animals)