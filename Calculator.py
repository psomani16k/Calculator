from tkinter import *


root = Tk()
root.title('Calculator')
display_text_var = StringVar()
display_text_var.set("Welcome to the calculator")
display = Label(root, bg="#000000", width='32', textvariable=display_text_var, height=3, fg='#ffffff')
display.grid(row=0, column=0, columnspan=4)
display_text=str()

## Defining functions and classes

def num_press(number):
    ##print('hi')
    global display_text
    display_text = display_text + number
    display_text_var.set(display_text)

def clean():
    global display_text
    display_text = ''
    display_text_var.set(display_text)

def back_space():
    global display_text
    display_text = display_text[:-1]
    ##print(display_text)
    display_text_var.set(display_text)

def symbol_press(symbol):
    global display_text
    size = len(display_text)
    ind = int(display_text.find('+')+display_text.find('-')+display_text.find('/')+display_text.find('*'))
    if display_text == '':
        pass
    elif display_text.find('+') == -1 and display_text.find('-') == -1 and display_text.find('/') == -1 and display_text.find('*') == -1 and display_text.find('%') == -1:
        num_press(symbol)
    else:
        if display_text[size-1:].isdigit() == False:
            back_space()
            num_press(symbol)
        else:
            pass

def decimal_point_press():
    global display_text
    if display_text.find('.') == -1:
        num_press('.')
    elif display_text.find('+') > display_text.find('.') or display_text.find('-') > display_text.find('.') or display_text.find('*') > display_text.find('.') or display_text.find('/') > display_text.find('.'):
        if display_text.count('.') == 1:
            num_press('.')
        else:
            pass
    else:
        pass

def calculate(symbol):
    global display_text
    if symbol == '=':
        if display_text.find('+') != -1:
            expresion_tup = display_text.partition('+')
            display_text = str(float(expresion_tup[0]) + float(expresion_tup[2]))
            ##print(display_text)
            display_text_var.set(display_text)
        elif display_text.find('-') != -1:
            expresion_tup = display_text.partition('-')
            display_text = str(float(expresion_tup[0]) - float(expresion_tup[2]))
            ##print(display_text)
            display_text_var.set(display_text)
        elif display_text.find('/') != -1:
            expresion_tup = display_text.partition('/')
            display_text = str(float(expresion_tup[0]) / float(expresion_tup[2]))
            ##print(display_text)
            display_text_var.set(display_text)
        elif display_text.find('*') != -1:
            expresion_tup = display_text.partition('*')
            display_text = str(float(expresion_tup[0]) * float(expresion_tup[2]))
            ##print(display_text)
            display_text_var.set(display_text)
    else:
        if display_text.find('/') != -1:
            expresion_tup = display_text.partition('/')
            display_text = str((float(expresion_tup[0]) / float(expresion_tup[2])) * 100) + '%'
            ##print(display_text)
            display_text_var.set(display_text)
        else:
            pass        

def bind_test(event):
    print(event.keysym)

## Defining buttons and binding

w,h = 7,3
afg, abg, fg, bg = 'black', 'white', 'white', 'black'

button_1 = Button(root, text='1', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('1'))
button_2 = Button(root, text='2', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('2'))
button_3 = Button(root, text='3', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('3'))
button_4 = Button(root, text='4', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('4'))
button_5 = Button(root, text='5', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('5'))
button_6 = Button(root, text='6', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('6'))
button_7 = Button(root, text='7', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('7'))
button_8 = Button(root, text='8', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('8'))
button_9 = Button(root, text='9', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('9'))
button_0 = Button(root, text='0', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: num_press('0'))
button_dec = Button(root, text='.', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=decimal_point_press)
button_back = Button(root, text='<-', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=back_space)
button_ac = Button(root, text='AC', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=clean)
button_add = Button(root, text='+', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: symbol_press('+'))
button_sub = Button(root, text='-', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: symbol_press('-'))
button_div = Button(root, text='/', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: symbol_press('/'))
button_mul = Button(root, text='*', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: symbol_press('*'))
button_per = Button(root, text='%', width=w, height=h, fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: calculate('%'))
button_equ = Button(root, text='=', width=w, height=(2*h+1), fg=fg, bg=bg, activebackground=abg, activeforeground=afg, command=lambda: calculate('='))



root.bind('1', lambda event: num_press('1'))
root.bind('2', lambda event: num_press('2'))
root.bind('3', lambda event: num_press('3'))
root.bind('4', lambda event: num_press('4'))
root.bind('5', lambda event: num_press('5'))
root.bind('6', lambda event: num_press('6'))
root.bind('7', lambda event: num_press('7'))
root.bind('8', lambda event: num_press('8'))
root.bind('9', lambda event: num_press('9'))
root.bind('0', lambda event: num_press('0'))
root.bind('.', lambda event: decimal_point_press())
root.bind('<BackSpace>', lambda event: back_space())
root.bind('<Delete>', lambda event: clean())
root.bind('<equal>', lambda event: symbol_press('+'))
root.bind('x', lambda event: symbol_press('*'))
root.bind('<slash>', lambda event: symbol_press('/'))
root.bind('<minus>', lambda event: symbol_press('-'))
root.bind('<Return>', lambda event: calculate('='))
root.bind('p', lambda event: calculate('%'))

button_ac.grid(row=1,column=0)
button_7.grid(row=2,column=0)
button_4.grid(row=3,column=0)
button_1.grid(row=4,column=0)
button_dec.grid(row=5,column=0)
button_back.grid(row=1,column=1)
button_8.grid(row=2,column=1)
button_5.grid(row=3,column=1)
button_2.grid(row=4,column=1)
button_0.grid(row=5,column=1)
button_div.grid(row=1,column=2)
button_9.grid(row=2,column=2)
button_6.grid(row=3,column=2)
button_3.grid(row=4,column=2)
button_per.grid(row=5,column=2)
button_mul.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_add.grid(row=3,column=3)
button_equ.grid(row=4,column=3, rowspan=2)

root.mainloop()