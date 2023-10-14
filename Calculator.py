from tkinter import*
win = Tk()
win.title('Calculator')
win.geometry('332x348')
win.resizable(0,0)

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clr():
    global expression
    expression = ''
    input_text.set('')
  
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ''
        
expression = ""
input_text = StringVar()

"""Text box frame"""
input_frame = Frame(win, width = 70, height = 10)
"""input_frame.pack(side = TOP)"""
input_frame.grid(row = 0, column = 0, sticky = 'w')

input_field = Entry(input_frame, font = ('arial', 20, 'bold'), width = 22, justify = RIGHT, textvariable = input_text)
input_field.grid(row = 0, column = 0)

"""increase the height"""
input_field.pack(ipady = 10)

"""Button frame"""
btns_frame = Frame(win, width = 43, height = 30)
btns_frame.grid(row = 1, column = 0, sticky = 'w')

sev = Button(btns_frame, text = '7', width = 10, height = 3, command = lambda: btn_click(7))
sev.grid(row = 0,column = 0,  padx =  1, pady = 1)
eight = Button(btns_frame, text = '8', width = 10, height = 3, command = lambda: btn_click(8))
eight.grid(row = 0,column = 1,  padx =  1, pady = 1)
nine = Button(btns_frame, text = '9', width = 10, height = 3, command = lambda: btn_click(9))
nine.grid(row = 0,column = 2, padx =  1, pady = 1)
clear = Button(btns_frame, text = 'C', width = 10, height = 3, command = lambda: btn_clr())
clear.grid(row = 0,column = 3, padx =  1, pady = 1)

four = Button(btns_frame, text = '4', width = 10, height = 3, command = lambda: btn_click(4))
four.grid(row = 1,column = 0, padx =  1, pady = 1)
five = Button(btns_frame, text = '5', width = 10, height = 3, command = lambda: btn_click(5))
five.grid(row = 1,column = 1, padx =  1, pady = 1)
six = Button(btns_frame, text = '6', width = 10, height = 3, command = lambda: btn_click(6))
six.grid(row = 1,column = 2, padx =  1, pady = 1)
X = Button(btns_frame, text = '*', width = 10, height = 3, command = lambda: btn_click('*'))
X.grid(row = 1,column = 3, padx =  1, pady = 1)

one = Button(btns_frame, text = '1', width = 10, height = 3, command = lambda: btn_click(1))
one.grid(row = 2,column = 0,  padx =  1, pady = 1)
two = Button(btns_frame, text = '2', width = 10, height = 3, command = lambda: btn_click(2))
two.grid(row = 2,column = 1, padx =  1, pady = 1)
three = Button(btns_frame, text = '3', width = 10, height = 3, command = lambda: btn_click(3))
three.grid(row = 2,column = 2, padx =  1, pady = 1)
div = Button(btns_frame, text = '/', width = 10, height = 3, command = lambda: btn_click('/'))
div.grid(row = 2,column = 3, padx =  1, pady = 1)

zero = Button(btns_frame, text = '0', width = 34, height = 3, command = lambda: btn_click(0))
zero.grid(row = 3,column = 0, columnspan = 3, padx =  1, pady = 1)
eq = Button(btns_frame, text = '=', width = 10, height = 7, command = lambda: btn_equal())
eq.grid(row = 3,column = 3, rowspan = 2, padx =  1, pady = 1)

dot = Button(btns_frame, text = '.', width = 10, height = 3, command = lambda: btn_click('.'))
dot.grid(row = 4,column = 0, padx =  1, pady = 1)
add = Button(btns_frame, text = '+', width = 10, height = 3, command = lambda: btn_click('+'))
add.grid(row = 4,column = 1, padx =  1, pady = 1)
sub = Button(btns_frame, text = '-', width = 10, height = 3, command = lambda: btn_click('-'))
sub.grid(row = 4,column = 2, padx =  1, pady = 1)

win.mainloop()