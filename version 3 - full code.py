# Python program to create a simple GUI
# Simple Quiz using Tkinter

#import everything from tkinter
from tkinter import *

# import messagebox from tkinter for pop up messages such as the score pop up
import tkinter.messagebox

# import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

#import csv to use csv file to store data
import csv

# Create a GUI Window
root = Tk()

# set the size of the GUI Window
root.geometry("1000x500")

# set the title of the Window
root.title("HTML/CSS Knowledge Quiz")

# unables the user form putting GUI Window in full screen mode
root.resizable(0, 0)

# This function is made to validate that all the required information is entered by the user in the registration form then changes the frame to the quiz if the user did.
def validate():
	while True:
		global name, age, country, gender
		name= name_entry.get()
		age = age_entry.get()
		country= country_entry.get()
		gender= gender_entry.get()
		if (name=="" or not (name.replace(" ", "").isalpha()) or (not (age.isnumeric() and (int(age) in range(12, 131)))) or country== 'Select your country'or gender == ""):
			tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty! and Invalid information is not acceptable")
			Clear()
			break

		else:
			tkinter.messagebox.showinfo('Success Message',"Successfully Saved")
			quiz()
			break

#This function delets the widgets on the registration for and runs the class for the question part of the program
def quiz():
	global quiz, frame #makes fram and quiz variables global to allow it to be used in other functions
	frame = Frame(root)
	frame.pack(side="top", expand=True, fill="both")

	#deltes the frame
	for widgets in frame.winfo_children():
		widgets.destroy()

	#runs quiz
	quiz = Quiz()

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

Button(root, text='Submit',width=15,bg='green',fg='black', command = validate).place(x=530,y=340)
Button(root, text='Clear',width=15,bg='#f33444',fg='black', command = Clear).place(x=350,y=340)
Button(root, text='Quit',width=10,bg='#ffffff',fg='black', command = root.destroy).place(x=460,y=380)

#class to define the components of the GUI for the Quiz
class Quiz:
	# This is the first method which is called when a new object of the class is initialized. This method sets the question count to 0. and initialize all the other methoods to display the content and make all the functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to display options for the current question
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(question)
		
		# keep a counter of correct answers
		self.correct=0


	# This method is used to display the result it counts the number of correct and wrong answers and then display them at the end as a message Box, it also adds the score of the user to the csv file at the end as this cannot be done when the user submits their information
	def display_result(self):
		# assigns the correct count
		correct = f"Correct: {self.correct}"

		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}")

		user_info = ['Name: {}'.format(name), '\t', 'Age: {}'.format(age), '\t', 'Country: {}'.format(country), '\t', 'Gender: {}'.format(gender), '\t' "{}".format(result)]

		with open("data.csv", "a") as file:
			writer = csv.writer(file, delimiter=' ')
			writer.writerow(user_info)


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# This method is used to check the answer of the current question by calling the check_ans and question no. if the question is correct it increases the count by 1 and then increase the question number by 1. If it is last question then it calls display result to show the message box. otherwise shows next question.
	def next_btn(self):
		global score
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			root.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()

	def quit(self):
		self.display_result()
		root.destroy()

	'''
	This method shows the two buttons on the screen.
	The first one is the next_button which moves to next question
	It has properties like what text it shows the functionality,
	size, color, and property of text displayed on button. Then it
	mentions where to place the button on the screen. The second
	button is the exit button which is used to close the GUI without
	completing the quiz.
	'''
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(root, text="Next",command=self.next_btn,
		width=10,bg="white",fg="black",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_button.place(x=450,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(root, text="Quit", command=self.quit, width=5,bg="white", fg="black",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=850,y=50)

	'''
	This method deselect the radio button on the screen then it is used to display the options available for the current
	question which we obtain through the question number and Updates
	each of the options for the current question of the radio button.
	'''
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(root, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(root, text="HTML/CSS Knowledge Quiz",
		width=80, bg="blue",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=-60, y=2)
        


	# This method shows the radio buttons to select the Question on the screen at the specified position. It also returns a list of radio button which are later used to add the options to them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(root,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40

		# return the radio buttons
		return q_list

	


with open('quiz_info.json') as f:
	data = json.load(f)

question = (data['ques'])
options = (data['choices'])
answer = (data[ 'ans'])

# Start the GUI
root.mainloop()


# END OF THE PROGRAM
