from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("400x300+20+10")

def btncolor():
    btn.configure(bg = "Yellow")

btn = Button(window, text = "Click to Change Color", command=btncolor)
btn.place(x = 130, y = 150)


window.mainloop()

