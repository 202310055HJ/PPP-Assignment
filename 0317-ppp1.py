print("과제 2번 문제입니다")
weight=int(input("몸무게를 입력하시오."))
height=int(input("키를 입력하시오."))
height_1 = height /100
import math
BMI=weight/ pow(height_1,2)
print(BMI)

if BMI >= 35:
    print("3단계 비만")
elif BMI >= 30:
    print("2단계 비만")
elif BMI >= 25:
    print("1단계 비만")
elif BMI >= 23:
    print("비만 전단계")
else:
    print("정상 체중")