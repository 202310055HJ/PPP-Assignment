def toggle_Ch(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90:
        return chr(ord(alphabet) + 32)
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122:
        return chr(ord(alphabet) - 32)

    return alphabet


def toggle_text(text: str) -> str:
    result = ""

    for c in text:
        result += toggle_Ch(c)

    return result


def main():
    ttext = input("아무 영문이나 입력하시오 : ")
    print(toggle_text(ttext))


if __name__ == "__main__":
    main()