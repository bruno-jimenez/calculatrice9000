import tkinter
from tkinter import *

root = Tk()
root.title("Calculatrice 9000")
root.resizable(width=False, height=False)
root.geometry("320x320")

a=Button(root, text="C", bg='#454545' , width=5, height=3, border=2)
a.grid(row=1, column=0)
# 7 8 9
b=Button(root, text="7", bg='grey', width=5, height=3, border=2)
b.grid(row=2, column=0)
# 4 5 6
c=Button(root, text="4", bg='gray', width=5, height=3, border=2)
c.grid(row=3, column=0)

g=Button(root, text="5", bg='grey', width=5, height=3, border=2)
g.grid(row=3, column=1)

g=Button(root, text="6", bg='grey', width=5, height=3, border=2)
g.grid(row=3, column=2)
# 1 2 3 
d=Button(root, text="1", bg='grey', width=5, height=3, border=2)
d.grid(row=4, column=0)

e=Button(root, text="2", bg='grey', width=5, height=3, border=2)
e.grid(row=4, column=1)

f=Button(root, text="3", bg='grey', width=5, height=3, border=2)
f.grid(row=4, column=2)

root.resizable(False, False)

root.mainloop()