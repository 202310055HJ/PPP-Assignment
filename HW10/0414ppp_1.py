def text2list(text):
    nums = text.split()
    nums = [int(n) for n in nums]
    return nums


def average(nums):
    return sum(nums) / len(nums)


def main():
    filename = input("파일 이름을 입력하세요: ")

    with open(filename, "r") as f:
        text = f.read().strip()

    print("읽은 텍스트:", text)

    nums = text2list(text)
    print("리스트:", nums)

    print("개수:", len(nums))
    print("평균:", average(nums))
    print("최댓값:", max(nums))
    print("최솟값:", min(nums))


if __name__ == "__main__":
    main()
