import math

print("각도  sin     cos     tan")

for i in range(0, 91, 10):
    rad = math.radians(i)

    sin_v = math.sin(rad)
    cos_v = math.cos(rad)

    if i == 90:
        tan_v = "정의X"
        print(f"{i:3}  {sin_v:.2f}  {cos_v:.2f}  {tan_v}")
    else:
        tan_v = math.tan(rad)
        print(f"{i:3}  {sin_v:.2f}  {cos_v:.2f}  {tan_v:.2f}")
