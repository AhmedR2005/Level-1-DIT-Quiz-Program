# Python program to create a simple GUI
# Simple Quiz using Tkinter

#import everything from tkinter
from tkinter import *

# import messagebox from tkinter for pop up messages such as the score pop up
import tkinter.messagebox

# Create a GUI Window
root = Tk()

# set the size of the GUI Window
root.geometry("1000x500")

# set the title of the Window
root.title("Registration Form")

# unables the user form putting GUI Window in full screen mode
root.resizable(0, 0)

#This function runs after the user presses submits, it checks if all the information entred by the user is valid or not and a pop up message shows according to the validity of the information
def validate():
    #calls the different user inputs and assigns them to a variable
    name= name_entry.get()
    age = age_entry.get()
    country= country_entry.get()
    gender= gender_entry.get()

    #This if statement sets different conditions, the users' information must not break to successfully submit their information.
    if (name=="" or not (name.replace(" ", "").isalpha()) or (not (age.isnumeric() and (int(age) in range(12, 130)))) or country== 'Select your country'or gender == ""):
    
        tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty! and Invalid information is not acceptable")
        Clear()

    else:
        tkinter.messagebox.showinfo('Success Message',"Successfully Saved")


#this function clears all the input boxes, radio buttons and droplist in the registration.
def Clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.set(None)
    country_entry.set("Select your country")

### This section places all the different widgets on the window and positions them ###
title_label = Label(root, text="Quiz Registration",width=40,font=("bold", 30))
title_label.place(x=140,y=53)

name_label = Label(root, text="Full Name",width=15,font=("bold", 15))
name_label.place(x=300,y=130)

name_entry = Entry(root)
name_entry.place(x=480,y=130)

age_label = Label(root, text="Age",width=15,font=("bold", 15))
age_label.place(x=300,y=180)

age_entry = Entry(root)
age_entry.place(x=480,y=180)

gender_label = Label(root, text="Gender",width=15,font=("bold", 15))
gender_label.place(x=300,y=230)
gender_entry = StringVar()
Radiobutton(root, text="Male",padx = 10, variable=gender_entry, value='Male').place(x=470,y=230)
Radiobutton(root, text="Female",padx = 40, variable=gender_entry, value='Female').place(x=600,y=230)

country_label = Label(root, text="Country",width=40,font=("bold", 15))
country_label.place(x=175,y=275)

countries = ['Canada','India','UK','Nepal','Iceland','South Africa','Other'];
country_entry=StringVar()
droplist=OptionMenu(root,country_entry, *countries)
droplist.config(width=20)
country_entry.set('Select your country') 
droplist.place(x=480,y=280)

Button(root, text='Submit',width=15,bg='blue',fg='black', command = validate).place(x=530,y=340)
Button(root, text='Clear',width=15,bg='grey',fg='black', command = Clear).place(x=350,y=340)
Button(root, text='Quit',width=10,bg='grey',fg='black', command = root.destroy).place(x=460,y=380)


# Start the GUI
root.mainloop()


# END OF THE PROGRAM
