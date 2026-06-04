import time

def countdown(s):
    sc = int(s)

    for i in range(sc, 0, -1):
        print(f"{i:3d}")
        time.sleep(1)

    print("time out")


def main():
    a = input("카운트 다운을 몇 초 진행하겠습니까. : ")
    countdown(a)


if __name__ == "__main__":
    main()