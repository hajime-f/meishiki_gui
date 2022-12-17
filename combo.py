#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

list1 = ['A','B','C','D']
list2 = ['1','2','3','4']

if __name__ == '__main__':
    root = Tk()
    root.title('Sample Program')

    # Frame
    frame = ttk.Frame(root, padding=30)
    frame.grid()

    lavel1 = Label(frame,font=("ＭＳ ゴシック",10),text="Select 1 :")
    lavel2 = Label(frame,font=("ＭＳ ゴシック",10),text="Select 2 :")
    lavel1.grid(row=0,column=0,sticky=W)
    lavel2.grid(row=1,column=0,sticky=W)

    v1 = StringVar()
    v2 = StringVar()
    cb1 = ttk.Combobox(
        frame, textvariable=v1, 
        values=list1, width=20)
    cb2 = ttk.Combobox(
        frame, textvariable=v2, 
        values=list2, width=20)

    cb1.set(list1[0])
    cb2.set(list2[0])


    cb1.bind(
        '<<ComboboxSelected>>', 
        lambda e: cb2.set(list2[list1.index(v1.get())]))
    cb1.grid(row=0, column=1)
    cb2.bind(
        '<<ComboboxSelected>>', 
        lambda e: print('v2=%s' % v2.get()))
    cb2.grid(row=1, column=1)

    root.mainloop()

    
