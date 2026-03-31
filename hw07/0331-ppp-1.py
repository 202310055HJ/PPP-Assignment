cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77, "사과": 60, "배": 55}

eat_dict = {"한라봉": 100, "딸기": 200, "바나나": 500}

total_cal = 0

for key, val in eat_dict.items():
    if key in cal_dict:
        total_cal += val * cal_dict[key] / 100

print(f"총 칼로리: {total_cal:.1f} kcal")