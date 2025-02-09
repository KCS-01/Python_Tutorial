# Quiz 2

bagPrice = input("가방 가격 : ")

watchPrice = input("시계 가격 : ")

totalPrice = int(bagPrice) + int(watchPrice)

discount = 0

if totalPrice >= 100000:
    discount = 0.3
elif totalPrice >= 50000:
    discount = 0.2
else:
    discount = 0.1
    
print("합계금액 : " + str(totalPrice * (1 - discount)))