from tkinter import Tk, Button, Label, mainloop


def call():
    print('fyvuvyfgyguybgft yf')


w = Tk()
w.minsize(400, 100)
w.geometry('300x200')

btn = Button(w, text='hello', command=call, height=2, width=20)
lbl = Label(w, text="new text", height=2, width=20)
btn.pack()
lbl.pack()

mainloop()
