from tkinter import *

root = Tk()
root.title("Calculatrice")
root.resizable(width=False, height=False)
root.geometry("258x480")
expression=""
equation= StringVar()

# affichage 
calcul_entry=Entry(root ,textvariable=equation, bg='white', font=10, foreground='black')
calcul_entry.grid(columnspan=4, ipadx=17, ipady=12)
calcul_entry.configure(state="readonly")

# V % ² / 

racine_button=Button(root, text="√", bg='#454545' , width=5, height=3, border=2, font=10,command=lambda: button_squareroot())
racine_button.grid(row=3, column=0)

modulo_button=Button(root, text="%", bg='#454545' , width=5, height=3, border=2, font=10,command=lambda:  button_click("//"))
modulo_button.grid(row=3, column=1)

carré_button=Button(root, text="²", bg='#454545' , width=5, height=3, border=2, font=10,command=lambda: button_square())
carré_button.grid(row=3, column=2)

division_button=Button(root, text="/", bg='#454545' , width=5, height=3, border=2, font=10,command=lambda: button_click("/"))
division_button.grid(row=3, column=3)

# 7 8 9 x

seven_button=Button(root, text="7", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("7"))
seven_button.grid(row=4, column=0)

eight_button=Button(root, text="8", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("8"))
eight_button.grid(row=4, column=1)

nine_button=Button(root, text="9", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("9"))
nine_button.grid(row=4, column=2)

multiplication_button=Button(root, text="x", bg='#454545' , width=5, height=3, border=2, font=10,command=lambda: button_click("*"))
multiplication_button.grid(row=4, column=3)

# 4 5 6 -

four_button=Button(root, text="4", bg='gray', width=5, height=3, border=2, font=10,command=lambda: button_click("4"))
four_button.grid(row=5, column=0)

five_button=Button(root, text="5", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("5"))
five_button.grid(row=5, column=1)

six_button=Button(root, text="6", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("6"))
six_button.grid(row=5, column=2)

soustraction_button=Button(root, text="-", bg='#454545', width=5, height=3, border=2, font=10,command=lambda: button_click("-"))
soustraction_button.grid(row=5, column=3)

# 1 2 3 +

one_button=Button(root, text="1", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("1"))
one_button.grid(row=6, column=0)

two_button=Button(root, text="2", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("2"))
two_button.grid(row=6, column=1)

three_button=Button(root, text="3", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("3"))
three_button.grid(row=6, column=2)

add_button=Button(root, text="+", bg='#454545', width=5, height=3, border=2, font=10,command=lambda: button_click("+"))
add_button.grid(row=6, column=3)

#C 0 . =

del_button=Button(root, text="C", bg='orange' , width=5, height=3, border=2, font=10,command=lambda: button_clear())
del_button.grid(row=7, column=0)

zero_button=Button(root, text="0", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("0"))
zero_button.grid(row=7, column=1)

virgule_button=Button(root, text=".", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("."))
virgule_button.grid(row=7, column=2)

egal_button=Button(root, text="=", bg='orange', width=5, height=3, border=2, font=10,command=lambda: button_equal())
egal_button.grid(row=7, column=3)
 
#button bind 
# Button function

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)


# Button for the "sqrt" operator

def button_squareroot():
    global expression
    expression = str(float(equation.get())**0.5)
    equation.set(expression)


# Button for the ² operator

def button_square():
    global expression
    expression = str(float(equation.get())**2)
    equation.set(expression)


def button_clear():
    global expression
    expression = ""
    equation.set("")


def button_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set('error')
        expression = ""

root.mainloop()