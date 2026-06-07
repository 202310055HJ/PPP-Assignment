import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def gui_input(msg):
    return simpledialog.askstring("입력", msg)


def gui_output(msg):
    messagebox.showinfo("결과", msg)


def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    ans = gui_input(f"{a} X {b} = ?")

    if ans == None:
        return False

    if int(ans) == a * b:
        return True
    else:
        return False


def main():
    root = tk.Tk()
    root.withdraw()

    score = 0

    for i in range(20):
        if gugudan_correct():
            score += 5

    gui_output(f"총 점수는 {score}점입니다.")

    root.destroy()


if __name__ == "__main__":
    main()