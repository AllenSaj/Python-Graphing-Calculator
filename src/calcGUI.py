from tkinter import *
from calcGraph import graph

app = Tk() 
app.geometry("340x370") 
app.resizable(0, 0) 
app.title("Calculator")

def buttonClick(item):
    global expression
    expression = expression + str(item)
    textBox.set(expression)

def buttonClear():
    global expression
    expression = "" 
    textBox.set("")
 
def buttonEqual():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    textBox.set(result)
    expression = ""

def buttonGraph():
    global expression
    textBox.set("")
    graph(expression)
    expression = ""

expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
textBox = StringVar()
 
# Let us creating a frame for the input field
textFrame = Frame(app, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
textFrame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
textField = Entry(textFrame, font=('arial', 18, 'bold'), textvariable=textBox, width=50, bg="#eee", bd=0, justify=RIGHT)
textField.grid(row=0, column=0)
textField.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
buttonFrame = Frame(app, width=312, height=272.5, bg="grey")
buttonFrame.pack()
 
clear = Button(buttonFrame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(buttonFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven = Button(buttonFrame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(buttonFrame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(buttonFrame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(buttonFrame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

four = Button(buttonFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(buttonFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(buttonFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(buttonFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick(" - ")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
one = Button(buttonFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(buttonFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(buttonFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(buttonFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick(" + ")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
zero = Button(buttonFrame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: buttonClick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttonFrame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(buttonFrame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick(" = ")).grid(row = 4, column = 3, padx = 1, pady = 1)

x = Button(buttonFrame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick("x")).grid(row = 5, column = 0, padx = 1, pady = 1)
y = Button(buttonFrame, text = "y", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick("y")).grid(row = 5, column = 1, padx = 1, pady = 1)
power = Button(buttonFrame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: buttonClick("**")).grid(row = 5, column = 2, padx = 1, pady = 1)
Graph = Button(buttonFrame, text = "Graph", fg = "red", width = 10, height = 3, bd = 0, bg = "#eed", cursor = "hand2", command = lambda: buttonGraph()).grid(row = 5, column = 3, padx = 1, pady = 1)

app.mainloop()


