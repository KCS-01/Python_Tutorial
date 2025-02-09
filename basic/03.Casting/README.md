# 입력과 자료형변환

```py
x = input("첫번째 숫자를 입력하세요 : ")
y = input("두번째 숫자를 입력하세요 : ")

print(x * y)

#Traceback (most recent call last):
#  File "/home/char1ey/char1ey/python_study/./03.Input/01.py", line 6, in <module>
#    print(x * y)
#TypeError: can't multiply sequence by non-int of type 'str'
```

## 에러의 발생이유

-   x와 y가 모두 숫자가 아닌 문자열로 들어가게됨, 이를 해결하기 위해서 자료형변환이 필요함
    -   input은 문자열로 입력하게됨

---

```py
year = int(input("태어난 연도를 입력해주세요 : "))
age = 2025 - year + 1

print("현재나이 :" + age)

#Traceback (most recent call last):
#  File "/home/char1ey/char1ey/python_study/03.Input/02.py", line 4, in <module>
#    print("현재나이 :" + age)
#TypeError: can only concatenate str (not "int") to str
```
