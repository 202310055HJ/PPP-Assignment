import tkinter as tk
from tkinter import simpledialog, messagebox

def gui_input(msg):
    return simpledialog.askstring("입력", msg)


def gui_output(msg):
    messagebox.showinfo("결과", msg)


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
    root = tk.Tk()
    root.withdraw()

    ttext = gui_input("아무 영문이나 입력하시오 : ")

    if ttext != None:
        result = toggle_text(ttext)
        gui_output(result)

    root.destroy()


if __name__ == "__main__":
    main()