print("과제 3번 문제입니다")

import math

ray = float(input("반지름을 입력하세요: "))

circumference = 2 * math.pi * ray
area = math.pi * ray ** 2

print(f"원의 둘레: {circumference:.1f}")
print(f"원의 면적: {area:.2f}")