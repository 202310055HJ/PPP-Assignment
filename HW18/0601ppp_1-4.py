import random

def make_lotto():
    numbers = []

    while len(numbers) < 6:
        num = random.randint(1, 45)

        if num not in numbers:
            numbers.append(num)

    numbers.sort()
    return numbers


def main():
    lotto = make_lotto()

    print("로또 번호 :", lotto)


if __name__ == "__main__":
    main()