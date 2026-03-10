from warnings import deprecated

print("Hello, World!")
name=("김현준")
print(name)
print("{}님 안녕하세요!".format(name))
print(f"{name}님 안녕하세요!")

department ="스마트팜학과"
print("{}({})님 안녕하세요!".format(name,department))
print(f"{name}({department})님 안녕하세요!")


T=100
print((T-32)*5/9)
result=(T-32)*5/9
print(f"{T}F=>{result}C")

print("과제 1번 문제입니다")
F=30
T=F/1.8+35
result2=(F/1.8)+35
print(f"{F}C=>{result2}F")

print("과제 2번 문제입니다")
weight=60
height=1.7
BMI=(weight/(height*height))
print(BMI)

print("과제 3번 문제입니다")
ray=4
O=(ray*ray*3.14)
print(O)

print("과제 4번 문제입니다")
LOW=5
TOP=3
Height=4
result4=(LOW+TOP)/2*Height
print(result4)

print("과제 5번 문제입니다")
thing=2000
discount=0.15
discount_rate=(thing*discount)
result5=(thing-discount_rate)
print(result5)