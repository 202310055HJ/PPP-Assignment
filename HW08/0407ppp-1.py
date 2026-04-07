def calc_calories(eat_dict, cal_dict):
    total = 0
    for key, val in eat_dict.items():
        if key in cal_dict:
            total += val * cal_dict[key] / 100
    return total


def main():
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
    eat_dict = {"한라봉": 100, "딸기": 200, "바나나": 500}

    result = calc_calories(eat_dict, cal_dict)
    print(f"총 칼로리: {result:.1f} kcal")


if __name__ == "__main__":
    main()