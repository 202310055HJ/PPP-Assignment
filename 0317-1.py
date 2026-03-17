import math

print("5번 과제입니다 두 지점 사이 거리를 구하시오")

x1=int(input("x1을 입력하세요:"))
y1=int(input("y1을 입력하세요:"))
x2=int(input("x2를 입력하세요:"))
y2=int(input("y2를 입력하세요:"))

distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("두 지점 사이의 거리",distance)
if(distance<1):print("두 점이 너무 가깝습니다")