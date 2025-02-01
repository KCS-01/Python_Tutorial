samsung = int(input("삼성전자 현재가격 : "))

if samsung >= 90000:
    print("매도합니다")
elif samsung >= 80000 and samsung < 90000:
    print("존버합니다")
elif samsung < 80000:
    print("살려주세요")