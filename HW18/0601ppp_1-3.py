import random

def main():
    words = ["apple", "banana", "school", "python", "computer"]
    answer = random.choice(words)

    hidden = ["_"] * len(answer)
    chance = 6

    while chance > 0:
        print("현재 단어 :", " ".join(hidden))
        print("남은 기회 :", chance)

        ch = input("알파벳을 입력하시오 : ")

        if ch in answer:
            for i in range(len(answer)):
                if answer[i] == ch:
                    hidden[i] = ch
        else:
            chance -= 1

        if "_" not in hidden:
            print("정답입니다.")
            print("단어는", answer, "입니다.")
            return

    print("실패했습니다.")
    print("정답은", answer, "입니다.")


if __name__ == "__main__":
    main()