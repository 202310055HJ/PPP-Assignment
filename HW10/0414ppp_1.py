def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


def get_count(nums):
    count = 0
    for _ in nums:
        count += 1
    return count


def get_max(nums):
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m


def get_min(nums):
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    return m


def median(nums):
    nums = sorted(nums)
    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n//2 - 1] + nums[n//2]) / 2


def main():
    filename = input("파일 이름을 입력하세요: ")

    nums = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                nums.append(int(line))

    print("리스트:", nums)
    print("개수:", get_count(nums))
    print("평균:", average(nums))
    print("최댓값:", get_max(nums))
    print("최솟값:", get_min(nums))
    print("중앙값:", median(nums))


if __name__ == "__main__":
    main()