import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def gui_input(msg):
    return simpledialog.askstring("입력", msg)


def gui_output(msg):
    messagebox.showinfo("결과", msg)


def main():
    root = tk.Tk()
    root.withdraw()

    words = ["apple", "banana", "school", "python", "computer"]
    answer = random.choice(words)

    hidden = ["_"] * len(answer)
    chance = 6

    while chance > 0:
        now = " ".join(hidden)

        ch = gui_input(f"현재 단어 : {now}\n남은 기회 : {chance}\n알파벳을 입력하시오 : ")

        if ch == None:
            break

        if ch in answer:
            for i in range(len(answer)):
                if answer[i] == ch:
                    hidden[i] = ch
        else:
            chance -= 1

        if "_" not in hidden:
            gui_output(f"정답입니다.\n단어는 {answer} 입니다.")
            root.destroy()
            return

    gui_output(f"실패했습니다.\n정답은 {answer} 입니다.")

    root.destroy()


if __name__ == "__main__":
    main()