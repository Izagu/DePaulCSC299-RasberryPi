from tkinter import *


def passGUI():
    window = Tk()



    window.title("Deactivation")



    window.geometry('350x200')



    lbl = Label(window, text="Please enter your password ")



    lbl.grid(column=1, row=3)



    txt = Entry(window,width=10)



    txt.grid(column=2, row=3)



    def clicked():


        res = txt.get()
        return (res)

    btn = Button(window, text="Click Me", command=clicked)



    btn.grid(column=3, row=3)



    window.mainloop

