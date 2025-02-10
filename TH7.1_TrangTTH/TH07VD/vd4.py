from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')

# Tạo nhãn (Label)
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm khi nút được nhấn
def clicked():
    lbl.configure(text="Button was clicked !!")

# Tạo nút bấm (Button) và liên kết với hàm clicked
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

# Chạy vòng lặp giao diện
window.mainloop()
