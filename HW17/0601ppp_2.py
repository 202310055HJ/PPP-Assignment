def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""

    for c in text:
        code = ord(c)

        if code >= 65 and code <= 90:
            code = code + shift

            if code > 90:
                code = code - 26

            result += chr(code)

        elif code >= 97 and code <= 122:
            code = code + shift

            if code > 122:
                code = code - 26

            result += chr(code)

        else:
            result += c

    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    result = ""

    for c in text:
        code = ord(c)

        if code >= 65 and code <= 90:
            code = code - shift

            if code < 65:
                code = code + 26

            result += chr(code)

        elif code >= 97 and code <= 122:
            code = code - shift

            if code < 97:
                code = code + 26

            result += chr(code)

        else:
            result += c

    return result


def main():
    text = input("문자열을 입력하시오 : ")

    secret = caesar_encode(text)
    origin = caesar_decode(secret)

    print("암호화 :", secret)
    print("복호화 :", origin)


if __name__ == "__main__":
    main()