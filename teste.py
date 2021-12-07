 #Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("500x300")

#Define functions
def display_msg():
   label.config(text="Résumé de l’ensemble du parc de voitures")

def show_list():
   listbox= Listbox(win, height=10, width= 40, bg= 'grey', activestyle= 'dotbox',font='aerial')
   listbox.insert(1,"nombre total de voitures")
   listbox.insert(1,"Num_T V L et Num_imma")
   listbox.insert(1,"Num_D et Num_imma")
   listbox.insert(1,"Le kilométrage moyen de l’ensemble des voitures")
   listbox.pack()
   button.destroy()

#Create a Label widget to display the message
label= Label(win, text= "", font= ('aerial 18 bold'))
label.pack(pady= 20)

#Define a Button widget
button= Button(win, text= "Click Here",command= lambda:[display_msg(), show_list()])
button.pack()
win.mainloop()