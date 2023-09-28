from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap("E:\me\Personal Development\Simple calculator GUI\calc.ico")
root.geometry("336x455")
root.configure(bg='white')
root.resizable(0, 0)
input_screen = PhotoImage(file="rect.png")
b_input_screen = Label(root, image=input_screen, borderwidth=0)
b_input_screen.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 4)
screen = Entry(root, borderwidth=0, width = 16, font=('Arial 22'))
screen.grid(row = 0, column = 0, padx = 10, pady = 9, columnspan = 4)

#-------Operations performed upon clicking a specific button-------
def click(num):
    screen.insert(END, num)

def delete():
    screen.delete(0, END)

def addition():
    if screen.get() == None:
        pass
    else:
        first_num = float(screen.get())
        global f_num
        f_num = first_num
        screen.delete(0, END)
        global operate
        operate = "addition"

def subtraction():
    if screen.get() == None:
        pass
    else:
        first_num = float(screen.get())
        global f_num
        f_num = first_num
        screen.delete(0, END)
        global operate
        operate = "subtraction"

def multiplication():
    if screen.get() == None:
        pass
    else:
        first_num = float(screen.get())
        global f_num
        f_num = first_num
        screen.delete(0, END)
        global operate
        operate = "multiplication"

def division():
    if screen.get() == None:
        pass
    else:
        first_num = float(screen.get())
        global f_num
        f_num = first_num
        screen.delete(0, END)
        global operate
        operate = "division"

def equal():
    s_num = float(screen.get())
    screen.delete(0, END)
    if operate == "addition":
        screen.insert(0, (f_num) + (s_num))
    elif operate == "subtraction":
        screen.insert(0, (f_num) - (s_num))
    elif operate == "multiplication":
        screen.insert(0, (f_num) * (s_num))
    else:
        screen.insert(0, (f_num) / (s_num))

#-------Adding images--------
one = PhotoImage(file="one.png")
two = PhotoImage(file="Two.png")
three = PhotoImage(file="Three.png")
four = PhotoImage(file="Four.png")
five = PhotoImage(file="Five.png")
six = PhotoImage(file="Six.png")
seven = PhotoImage(file="Seven.png")
eight = PhotoImage(file="Eight.png")
nine = PhotoImage(file="mine.png")
zero = PhotoImage(file="Zero.png")
plus = PhotoImage(file="plus.png")
minus = PhotoImage(file="minus.png")
divide = PhotoImage(file="divide.png")
multiply = PhotoImage(file="multiply.png")
clear = PhotoImage(file="clear.png")
Decimal = PhotoImage(file="decimal.png")
Equal = PhotoImage(file="equal.png")

#-------Creating all buttons-------
b_1 = Button(root, image=one, command=lambda: click(1), borderwidth=0)
b_2 = Button(root, image=two, command=lambda: click(2), borderwidth=0)
b_3 = Button(root, image=three, command=lambda: click(3), borderwidth=0)
b_4 = Button(root, image=four, command=lambda: click(4), borderwidth=0)
b_5 = Button(root, image=five, command=lambda: click(5), borderwidth=0)
b_6 = Button(root, image=six, command=lambda: click(6), borderwidth=0)
b_7 = Button(root, image=seven, command=lambda: click(7), borderwidth=0)
b_8 = Button(root, image=eight, command=lambda: click(8), borderwidth=0)
b_9 = Button(root, image=nine, command=lambda: click(9), borderwidth=0)
b_0 = Button(root, image=zero, command=lambda: click(0), borderwidth=0)
b_add = Button(root, image=plus, command= addition, borderwidth=0)
b_sub = Button(root, image=minus, command= subtraction, borderwidth=0)
b_mul = Button(root, image=multiply, command= multiplication, borderwidth=0)
b_div = Button(root, image=divide, command= division, borderwidth=0)
b_eqv = Button(root, image=Equal, command=equal, height=300, borderwidth=0)
b_dec = Button(root, image=Decimal, command=lambda: click("."), borderwidth=0)
b_del = Button(root, image=clear, command= delete, borderwidth=0)

#-------Placing all buttons-------
b_add.grid(row = 1, column = 0)
b_sub.grid(row = 1, column = 1)
b_div.grid(row = 1, column = 2)
b_del.grid(row = 5, column = 0)
b_7.grid(row = 2, column = 0)
b_8.grid(row = 2, column = 1)
b_9.grid(row = 2, column = 2)
b_4.grid(row = 3, column = 0)
b_5.grid(row = 3, column = 1)
b_6.grid(row = 3, column = 2)
b_1.grid(row = 4, column = 0)
b_2.grid(row = 4, column = 1)
b_3.grid(row = 4, column = 2)
b_mul.grid(row = 1, column = 3)
b_0.grid(row = 5, column = 1)
b_dec.grid(row = 5, column = 2)
b_eqv.grid(row = 2, column = 3, rowspan = 4)


mainloop()



