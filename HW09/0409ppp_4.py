def main():
    nums = input("숫자들을 입력하세요: ").split()


    nums = [float(x) for x in nums]
    avg = average(nums)

    print(f"평균: {avg:.2f}")