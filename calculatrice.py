from tkinter import *

root = Tk()

a=Label(root, text="A", bg='red', width=5, height=5)
a.grid(row=1, column=0)
# 7 8 9
b=Label(root, text="7", bg='lightblue', width=5, height=5)
b.grid(row=2, column=0)
# 4 5 6
c=Label(root, text="4", bg='gray', width=5, height=5)
c.grid(row=3, column=0)

g=Label(root, text="5", bg='green', width=5, height=5)
g.grid(row=3, column=1)

g=Label(root, text="6", bg='green', width=5, height=5)
g.grid(row=3, column=2)
# 1 2 3 
d=Label(root, text="1", bg='blue', width=5, height=5)
d.grid(row=4, column=0)

e=Label(root, text="2", bg='lime', width=5, height=5)
e.grid(row=4, column=1)

f=Label(root, text="3", bg='orange', width=5, height=5)
f.grid(row=4, column=2)

root.resizable(False, False)

root.mainloop()