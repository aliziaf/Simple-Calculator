from tkinter import *
import tkinter.messagebox

#--------------Setting-------------
main_page = Tk()
main_page.geometry("500x240")
main_page.title("Calculator")
main_page.resizable(width=False , height=False)
main_page.configure(bg = 'gray') # BackGroung Color

#--------------Variables---------------
num1 = StringVar()
num2 = StringVar()
res_num = StringVar()
#--------------Functions---------------
def errorinput(message):
    if message == "error":
        tkinter.messagebox.showerror('error' , 'It is wrong Number!')
    elif message == "Bad Division!" :
        tkinter.messagebox.showerror('error' , 'It is wrong Number --> 0')


def plusnums():
    try:
        value = float(num1.get()) + float(num2.get())
        res_num.set(value)
    except: 
        errorinput("error")       

def minusnums():
    try:
        value = float(num1.get()) - float(num2.get())
        res_num.set(value)
    except: 
        errorinput("error") 

def multiplenums():
    try:
        value = float(num1.get()) * float(num2.get())
        res_num.set(value)
    except: 
        errorinput("error") 

def dividenums():
    if num2.get() == '0':
        errorinput('Bad Division!')
    elif num2.get():
        try:
            value = float(num1.get()) / float(num2.get())
            res_num.set(value)
        except: 
            errorinput("error") 

#--------------Make Frames---------------
first_frame = Frame(main_page , width=500, height=60 , bg='gray')
first_frame.pack(side=TOP) # Top of GUI

second_frame = Frame(main_page , width=500, height=60 , bg='gray')
second_frame.pack(side=TOP) 

third_frame = Frame(main_page , width=500, height=60 , bg='blue')
third_frame.pack(side=TOP) 

forth_frame = Frame(main_page , width=500, height=60 , bg='gray')
forth_frame.pack(side=TOP) 

#--------------Create Buttons---------------

plus = Button(third_frame, text="+", width=10,
                  highlightbackground='gray', command=lambda: plusnums())
plus.pack(side=LEFT, padx=10, pady=10)

minus = Button(third_frame , text="-" , highlightbackground= 'yellow', width=10, command=lambda:minusnums()) # master is the specific frame
minus.pack(side=LEFT,padx=5 , pady=5)

multiple = Button(third_frame , text="*" , highlightbackground= 'yellow', width=10, command=lambda:multiplenums()) # master is the specific frame
multiple.pack(side=LEFT,padx=5 , pady=5)

divide = Button(third_frame , text="/" , highlightbackground= 'yellow', width=10, command=lambda:dividenums()) # master is the specific frame
divide.pack(side=LEFT,padx=5 , pady=5)

#--------------Inputs---------------
first_label = Label(first_frame , text="Num1" , bg='gray') 
first_label.pack(side=LEFT, pady=5 , padx=5)
first_num = Entry(first_frame , highlightbackground= 'yellow' , textvariable=num1)
first_num.pack(side=LEFT)

second_label = Label(second_frame , text="Num2" , bg='gray') 
second_label.pack(side=LEFT, pady=5 , padx=5)
second_num = Entry(second_frame , highlightbackground= 'yellow', textvariable=num2)
second_num.pack(side=LEFT)

result = Label(forth_frame , text="Result:" , bg='gray') 
result.pack(side=LEFT, pady=5 , padx=5)
result_num = Entry(forth_frame , highlightbackground= 'yellow', textvariable=res_num)
result_num.pack(side=LEFT)



main_page.mainloop()




