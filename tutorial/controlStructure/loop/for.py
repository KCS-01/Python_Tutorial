score = [90, 25, 67, 45, 80]

for student in score:
    if student >= 60:
        print("%d점이므로 합격" % student)
    else:
        print("%d점이므로 불합격" % student)
        
for student in score:
    if student < 60:
        continue
    print("%d 점 ㅊㅋㅊㅋ" % student)
    
a = range(10)

print(a)


add = 0

for i in range(1, 11):
    add += i

print(add)

for number in range(len(score)):
    if score[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
    

a = [1, 2, 3, 4]

result = [num * 3 for num in a]

print(result) # [3, 6, 9, 12]

for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
    
    
    
    
result2 = [ x*y for x in range(2,10)
                for y in range(1,10)]

print(result2)
