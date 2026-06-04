import random

def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    ans = input(f"{a} X {b} = ? --> ")

    return int(ans) == a * b


def main():
    score = 0

    for i in range(20):
        if gugudan_correct():
            score += 5

    print(f"총 점수는 {score}점입니다.")


if __name__ == "__main__":
    main()