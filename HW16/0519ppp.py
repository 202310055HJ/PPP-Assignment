numbers = []

while True:
    x = input("X=? ")

    try:
        x = int(x)

        if x == -1:
            break

        if x > 0:
            numbers.append(x)

    except:
        pass

count = len(numbers)
avg = sum(numbers) / count

print(f"입력된 값은 {numbers} 입니다. 총 {count}개의 자연수가 입력되었고, 평균은 {avg}입니다.")