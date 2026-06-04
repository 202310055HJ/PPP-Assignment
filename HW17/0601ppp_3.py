import random

def get_chosung(word):
    chosung = [
        "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ",
        "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
        "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ",
        "ㅋ", "ㅌ", "ㅍ", "ㅎ"
    ]

    result = ""

    for c in word:
        code = ord(c)

        if code >= ord("가") and code <= ord("힣"):
            index = (code - ord("가")) // 588
            result += chosung[index]
        else:
            result += c

    return result


def main():
    words = ["사과", "바나나", "컴퓨터", "학교", "파이썬", "자동차", "강아지"]

    answer = random.choice(words)
    hint = get_chosung(answer)

    print("초성 :", hint)

    user = input("정답을 입력하시오 : ")

    if user == answer:
        print("정답입니다.")
    else:
        print("틀렸습니다.")
        print("정답은", answer, "입니다.")


if __name__ == "__main__":
    main()