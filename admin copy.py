from tkinter import *
import tkinter
window = Tk()
window.title("2F")
lbl=Label(window, text="2F System", fg='red', font=("Helvetica", 16))
lbl.place(x=100, y=80)

# You will create two text labels namely 'username' and 'password' and and two input labels for them

tkinter.Label(window, text = "Username").grid(row = 0) #'username' is placed on position 00 (row - 0 and column - 0)

# 'Entry' class is used to display the input-field for 'username' text label
tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

tkinter.Label(window, text = "Password").grid(row = 1) #'password' is placed on position 10 (row - 1 and column - 0)

tkinter.Entry(window).grid(row = 1, column = 1) #second input-field is placed on position 11 (row - 1 and column - 1)

# 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid( columnspan = 5 ) 
btn=Button(window, text="Open", fg='blue')
btn.place(x=120, y=150)                
window.geometry("300x200+10+10")

window.mainloop()