print("과제 2번입니다")

x = int(input("x 값을 입력하세요: "))
y = int(input("y 값을 입력하세요: "))

if x > 0 and y > 0:
    print(f"입력한 좌표({x}, {y})는 1사분면입니다.")

elif x < 0 and y > 0:
    print(f"입력한 좌표({x}, {y})는 2사분면입니다.")

elif x < 0 and y < 0:
    print(f"입력한 좌표({x}, {y})는 3사분면입니다.")

elif x > 0 and y < 0:
    print(f"입력한 좌표({x}, {y})는 4사분면입니다.")
else:
    print("축 위에 있는 점입니다.")