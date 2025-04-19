# 딕셔너리 관련 함수

# 1. Key 리스트 만들기 - keys

a = {'name' : 'char1ey', 'age': 31}

keyList = a.keys()

print(keyList) # --> dict_keys(['name', 'age'])
print(list(keyList))

for key in keyList:
    print(key)
    
valueList = a.values()
print(valueList)


itemList = a.items()
print(itemList)

a.clear()
print(a)

name = a.get('name')
phone = a.get('phone')

print(name)
print(phone)

defaluePhone = a.get('phone', '010-1234-5678')
print(defaluePhone)

exam = {'name': 'char2ey', 'age': 31}

isName ='name' in exam
isEmail = 'email' in exam

print(isName)
print(isEmail)