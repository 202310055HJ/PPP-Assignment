import random
import tkinter as tk
from tkinter import messagebox

def gui_output(msg):
    messagebox.showinfo("결과", msg)


def make_lotto():
    numbers = []

    while len(numbers) < 6:
        num = random.randint(1, 45)

        if num not in numbers:
            numbers.append(num)

    numbers.sort()
    return numbers


def main():
    root = tk.Tk()
    root.withdraw()

    lotto = make_lotto()

    gui_output(f"로또 번호 : {lotto}")

    root.destroy()


if __name__ == "__main__":
    main()