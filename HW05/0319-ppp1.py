

print("변환 가능 프로그램")
print("1. 화씨 -> 섭씨")
print("2.섭씨 -> 화씨")
print("3. 피트(ft) -> cm")
print("4. cm -> 피트(ft)")

choice = int(input("번호를 입력하십시오:"))
if choice == 1:
    f = float(input("화씨의 온도 입력:"))
    c = (f - 32) * 5/9
    print(f"섭씨 온도: {c:.1f}")

elif choice == 2:
    c = float(input("섭씨 온도 입력: "))
    f = c * 9 / 5 + 32
    print(f"화씨 온도: {f:.1f}")

elif choice == 3:
    ft = float(input("피트(ft) 입력: "))
    cm = ft * 30.48
    print(f"cm: {cm:.1f}")

elif choice == 4:
    cm = float(input("cm 입력: "))
    ft = cm / 30.48
    print(f"피트(ft): {ft:.1f}")

else:
    print("잘못된 입력입니다.")
