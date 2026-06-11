from tkinter import *

def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get().replace("^", "**"))
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = Entry(root, width=25, font=("Arial", 20))
entry.pack(pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','%','^','+'
]

frame = Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    Button(frame, text=button, width=5, height=2,
           command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="=", width=20, command=calculate).pack(pady=5)
Button(root, text="C", width=20, command=clear).pack(pady=5)

root.mainloop()
