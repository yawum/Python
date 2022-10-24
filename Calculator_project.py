# Yves Awum
# Final Project


from tkinter import *

win = Tk()
# Now we create a frame for the calculator and give it a title/name
win.geometry("450x650")
win.resizable(0,0)
win.title("mypython Calc.")
winlabel = Label(win, text="CALCULATOR", bg='dark gray', font = ("Times", 13,'bold'))
winlabel.pack(side=TOP)
win.config(background='dark gray')

# functions starts here
# btn_click updates the input field whenever a button is clicked

expression = ""    
input_text = StringVar()
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)


def btn_click(item):  #lambda:btn_click (1)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
 
 #btn_clear function clear the screen
 
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
    
def btn_equal():
    global expression
    result = str(eval(expression)) #eval is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
    
def btn_add():
    global expression
    result = str(eval(expression)) 
    input_text.set(add)
    expression = ""


def btn_sub():
    global expression
    result = str(eval(expression)) 
    input_text.set(sub)
    expression = ""

def btn_mul():
    global expression
    result = str(eval(expression)) 
    input_text.set(mul)
    expression = ""

def btn_div():
    global expression
    result = str(eval(expression)) 
    input_text.set(div)
    expression = ""




#Creating a small window for input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win, width=350, height=315, bg="grey")
btns_frame.pack()

# row number1
clear = Button(btns_frame, text = "C", fg = "black", width = 25, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# row number2
seven = Button(btns_frame, text = "7", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# row number3

four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


# row number4

three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 2, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 2, column = 1, padx = 1, pady = 1)
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 2, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 2, column = 3, padx = 1, pady = 1)


# row number5
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal("=")).grid(row = 4, column = 3, padx = 1, pady = 1)
 


win.mainloop()

 