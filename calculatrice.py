import tkinter
from tkinter import *

root = Tk()
root.title("Calculatrice")
root.resizable(width=False, height=False)
root.geometry("258x532")
expression= ''
equation= StringVar()
result= StringVar()

# affichage
calcul_entry=Entry(root ,textvariable=equation, bg='white', font=10, foreground='lightgrey')
calcul_entry.grid(columnspan=4, ipadx=17, ipady=12)
calcul_entry.configure(state="readonly")

result_entry=Entry(root ,textvariable=result, bg='white', font=10, foreground='black')
result_entry.grid(columnspan=4,ipadx=17, ipady=12)
result_entry.configure(state="readonly")
# V / * 
racine_button=Button(root, text="√", bg='#454545' , width=5, height=3, border=2, font=10)
racine_button.grid(row=3, column=0)

modulo_button=Button(root, text="%", bg='#454545' , width=5, height=3, border=2, font=10)
modulo_button.grid(row=3, column=1)

carré_button=Button(root, text="²", bg='#454545' , width=5, height=3, border=2, font=10)
carré_button.grid(row=3, column=2)

division_button=Button(root, text="/", bg='#454545' , width=5, height=3, border=2, font=10)
division_button.grid(row=3, column=3)
# 7 8 9 x

seven_button=Button(root, text="7", bg='grey', width=5, height=3, border=2, font=10)
seven_button.grid(row=4, column=0)

eight_button=Button(root, text="8", bg='grey', width=5, height=3, border=2, font=10)
eight_button.grid(row=4, column=1)

nine_button=Button(root, text="9", bg='grey', width=5, height=3, border=2, font=10)
nine_button.grid(row=4, column=2)

multiplication_button=Button(root, text="x", bg='#454545' , width=5, height=3, border=2, font=10)
multiplication_button.grid(row=4, column=3)

# 4 5 6 -

four_button=Button(root, text="4", bg='gray', width=5, height=3, border=2, font=10)
four_button.grid(row=5, column=0)

five_button=Button(root, text="5", bg='grey', width=5, height=3, border=2, font=10)
five_button.grid(row=5, column=1)

six_button=Button(root, text="6", bg='grey', width=5, height=3, border=2, font=10)
six_button.grid(row=5, column=2)

soustraction_button=Button(root, text="-", bg='#454545', width=5, height=3, border=2, font=10)
soustraction_button.grid(row=5, column=3)

# 1 2 3 +

one_button=Button(root, text="1", bg='grey', width=5, height=3, border=2, font=10)
one_button.grid(row=6, column=0)

two_button=Button(root, text="2", bg='grey', width=5, height=3, border=2, font=10)
two_button.grid(row=6, column=1)

three_button=Button(root, text="3", bg='grey', width=5, height=3, border=2, font=10)
three_button.grid(row=6, column=2)

add_button=Button(root, text="+", bg='#454545', width=5, height=3, border=2, font=10)
add_button.grid(row=6, column=3)

#C 0 . =

del_button=Button(root, text="C", bg='orange' , width=5, height=3, border=2, font=10)
del_button.grid(row=7, column=0)

zero_button=Button(root, text="0", bg='grey', width=5, height=3, border=2, font=10)
zero_button.grid(row=7, column=1)

virgule_button=Button(root, text=".", bg='grey', width=5, height=3, border=2, font=10)
virgule_button.grid(row=7, column=2)

egal_button=Button(root, text="=", bg='orange', width=5, height=3, border=2, font=10)
egal_button.grid(row=7, column=3)

root.resizable(False, False)

root.mainloop()