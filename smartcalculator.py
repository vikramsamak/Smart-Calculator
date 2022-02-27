from msilib.schema import Icon
from tkinter import *
import tkinter

#CALCULATION_FUNCTION
def calculate():
        try:
            num1 = n1entry.get()
            num2 = n2entry.get()
            num1 = float(num1)  
            num2 = float(num2)
            addition = num1+num2
            substraction = num1-num2
            multiplication = num1*num2
            division = num1/num2
            add.insert(0,addition)
            sub.insert(0,substraction)
            mul.insert(0,multiplication)
            div.insert(0, division)
        except ValueError:
            n1entry.delete(0,END)
            n2entry.delete(0,END)
            error_message = "Invalid Entry"
            n1entry.insert(0, error_message)
            n2entry.insert(0, error_message)
def resetall():
    n1entry.delete(0,END)
    n2entry.delete(0,END)
    add.delete(0,END)
    sub.delete(0,END)
    mul.delete(0, END)
    div.delete(0,END)
    
def darkmode(dark):    
    dark=darkmode.get()
    dark=int(dark)
  
    if dark==1:
        window.config(bg='black')
        inputframe.config(bg='black',fg='white')
        outputframe.config(bg='black',fg='white')
        label1.config(fg='white',bg='black')
        label2.config(fg='white',bg='black')
        btn.config(fg='white',bg='black')
        l1.config(fg='white',bg='black')            
        l2.config(fg='white', bg='black') 
        l3.config(fg='white', bg='black')
        l4.config(fg='white',bg='black')
        btn2.config(fg='white',bg='black')
        darkmode.config(fg='white',bg='black')
        darkmodelabel.config(fg='white', bg='black')
        name.config(fg='white', bg='black')
        infolabel.config(fg='white', bg='black')
    else:
        window.config(bg='white')
        inputframe.config(bg='white', fg='black')
        outputframe.config(bg='white', fg='black')
        label1.config(bg='white', fg='black')
        label2.config(bg='white', fg='black')
        btn.config(bg='white', fg='black')
        l1.config(bg='white', fg='black')
        l2.config(bg='white', fg='black') 
        l3.config(bg='white', fg='black')
        l4.config(bg='white', fg='black')
        btn2.config(bg='white', fg='black')
        darkmode.config(bg='white', fg='black')
        darkmodelabel.config(bg='white', fg='black')
        name.config(bg='white', fg='black')
        infolabel.config(bg='white', fg='black')
            
        


#UI_PART
#WINDOW
window = tkinter.Tk()
window.title("SMART CALCULATOR")
window.geometry('650x650')



#INPUT_UI
inputframe = LabelFrame(window,text="Inputs",bd=3,width=60)
inputframe.pack()
label1 = Label(inputframe, text="Enter First Number",)
label1.pack()
n1entry = Entry(inputframe,width=60,bd=3)
n1entry.pack(pady=10)

label2 = Label(inputframe, text = "Enter Second Number",)
label2.pack(pady=10)
n2entry = Entry(inputframe,width=60,bd=3)
n2entry.pack(pady=10)

btn = Button(inputframe, text="CALCULATE", command=calculate, width=31)
btn.pack(pady=10)

#OUTPUT_UI
outputframe = LabelFrame(window, text="Outputs", bd=3, width=60)
outputframe.pack()
l1=Label(outputframe, text="Addition")
l1.pack()

add = Entry(outputframe, width=60, bd=3)
add.pack()

l2 = Label(outputframe, text="Substraction")
l2.pack(pady=10)
sub = Entry(outputframe, width=60, bd=3)
sub.pack()

l3=Label(outputframe, text="Multiplication")
l3.pack(pady=10)
mul = Entry(outputframe, width=60, bd=3)
mul.pack()

l4 = Label(outputframe,text="Division")
l4.pack(pady=10)
div = Entry(outputframe, width=60, bd=3)
div.pack()

btn2=Button(window, text="RESET", width=31,command = resetall)
btn2.pack(pady=10)


darkmodelabel=Label(window,text="DARKMODE SWITCH")
darkmodelabel.pack()
darkmode = Scale(window,from_=0,to=1,orient=HORIZONTAL,command=darkmode)
darkmode.pack()
infolabel=Label(window,text="0-Normal Mode 1-Dark Mode")
infolabel.pack()
name=Label(window, text="Designed And Developed By Vikram Samak")
name.pack()


window.mainloop()