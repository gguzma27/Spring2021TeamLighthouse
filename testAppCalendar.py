#Test GUI for COVID-19 results reporting
#Created by Team Lighthouse
#Date: 03/21/2021
#Revision date: 03/21/2021

# Notes: from Glenn Guzman-Rockett
# -The individual Pages are built out as frames, that get pulled to front view 
#   when called by the buttons
# -As of right now(9:30am, 3/22/21) there are a LOT of placeholders for functionality
# -The original template used grid() to space everything, but pack() seems to accomplish
#   what we need
# -Looking into tkcalender to add scheduling for the scheduling screens
#   UPDATE: Added some interactive calendars to the scheduling screens
#  3/22/21
# -Added time selection to Calendars in both scheduling screens
#   3/24/21

from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import dbLink
import yearBuild


#This font was used early in the script can be used again
#just haven't really looked at it

LARGEFONT =("Verdana", 35)

global User_first_name
global User_last_name
global User_DOB
global results

results = ""
User_first_name = ""
User_DOB = ""
User_last_name = ""




class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_rowconfigure(1, weight = 1)
		container.grid_rowconfigure(2, weight = 1)
		container.grid_rowconfigure(3, weight = 1)
		container.grid_rowconfigure(4, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		container.grid_columnconfigure(1, weight = 1)
		container.grid_columnconfigure(2, weight = 1)
		container.grid_columnconfigure(3, weight = 1)
		container.grid_columnconfigure(4, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2,Page3,Page4,Page5,Page6,Page7,Page8,Page9,Page10):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		#frame.winfo_toplevel().geometry("800x400")
		#^^^ early attempt to "fix" the window size, could be used later

# first window frame startpage, this will be the welcome page
class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, anchor="center",width=-100,text ="Welcome to\nOSF Healthcare!",justify=tk.CENTER,background="white",padding = 50)#,font = LARGEFONT)
		
		#Used a White background to get a sense of the space of the label
		
		# putting the label in its place by using
		# using pack
		label.pack(side="top",fill="x")
		
		button1 = ttk.Button(self, text ="Click Here\nto Begin",command = lambda : controller.show_frame(Page1))
		
	
		# putting the button in its place by
		# using pack
		button1.pack(side="bottom")




# second window frame page1, our verfication page
# this will be a pass through for now: 03/22/2021 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",width=-100,text ="Are you a\nnew user?" ,justify=tk.CENTER,background="white",padding = 50)
		
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Yes",
							command = lambda : controller.show_frame(Page8))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="No",
							command = lambda : controller.show_frame(Page9))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")




# third window frame page2
# our main menu

class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		
		def findResults():
			global results
			global User_first_name
			global User_last_name
			results = dbLink.getResults(User_first_name,User_last_name)
			print(User_first_name + " " +User_last_name+" "+results)
			controller.show_frame(Page5)
		
		tk.Frame.__init__(self, parent)
		
		#added icons for Menu Buttons
		self.my_img = ImageTk.PhotoImage(Image.open("images/calendar1.png"))
		self.resultsImg = ImageTk.PhotoImage(Image.open("images/resultsAdj.png"))

		
		label = ttk.Label(self, anchor="n",text ="Main Menu",width=-80, justify=tk.CENTER)
		label.grid(row = 0,column = 1,columnspan=3, padx = 10, pady = 10,sticky="ew")
		
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self,image=self.my_img,compound = tk.BOTTOM,text ="Schedule Test",command = lambda : controller.show_frame(Page3))
	
							
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 0, ipadx = 10, ipady = 10)
	
		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self,image=self.my_img,compound = tk.BOTTOM, text ="Schedule Vaccine",command = lambda : controller.show_frame(Page4))
		
							
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 2, ipadx = 10, ipady = 10)
			
		
		button3 = ttk.Button(self,image=self.resultsImg, compound = tk.BOTTOM, text="See Results", command = findResults)
		button3.grid(row = 1, column = 4, ipadx = 10, ipady = 5)
		

#page 3 is where we will schedule appts
class Page3(tk.Frame): 
	def __init__(self, parent, controller):
	
		#assignment functions to make variables out of user selection
		def date_assign(e):
			apptDay = str(cal.get_date())
		
		def time_assign(e):
			apptTime = str(cb.get())
			
		tk.Frame.__init__(self, parent)
		
		#Calendar Section
		
		cal = Calendar(self, selectmode='day', date_pattern = 'y/mm/dd')
		cal.pack(fill="both", expand=True)
		global apptDay
		global apptTime
		
		#Time Slot Section
		cal.var = tk.StringVar()
		options = ["11:00", "11:15", "11:30", "11:45",
		           "12:00", "12:15", "12:30", "12:45",
		           "01:00", "01:15", "01:30", "01:45",
		           "02:00", "02:15", "02:30", "02:45"]
		cb = ttk.Combobox(cal, textvariable=cal.var, values=options)
		cb.current(0)
		cb.pack(side="top")
		
		#both the calender and combobox are bound to selection events
		cal.bind("<<CalendarSelected>>",date_assign)
		cb.bind("<<ComboboxSelected>>",time_assign)
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Next",
							command = lambda : controller.show_frame(Page6))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		
#page 4 is where we will schedule vaccines
class Page4(tk.Frame): 
	def __init__(self, parent, controller):
		
		#assignment functions to make variables out of user selection
		def date_assign(e):
			vacDay = str(cal.get_date())
		
		def time_assign(e):
			vacTime = str(cb.get())
			
	
		tk.Frame.__init__(self, parent)
		
		#Calendar section, set to day selection
		cal = Calendar(self, selectmode='day', date_pattern = 'y/mm/dd')
		cal.pack(fill="both", expand=True)
		global vacDay
		global vacTime
		
		#Time Slot section
		cal.var = tk.StringVar()
		options = ["11:00", "11:15", "11:30", "11:45",
		           "12:00", "12:15", "12:30", "12:45",
		           "01:00", "01:15", "01:30", "01:45",
		           "02:00", "02:15", "02:30", "02:45"]
		cb = ttk.Combobox(cal, textvariable=cal.var, values=options)
		cb.current(0)
		cb.pack(side="top")
		
		#both the calender and combobox are bound to selection events
		cal.bind("<<CalendarSelected>>",date_assign)
		cb.bind("<<ComboboxSelected>>",time_assign)
		
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Next",
							command = lambda : controller.show_frame(Page6))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		
#page 5 is where we will see results
class Page5(tk.Frame): 
	def __init__(self, parent, controller):
		
		
		def updateResults():
			global results
			
			if results == "yes":
				return "You have tested positive for COVID-19"
			elif results == "no":
				return "You have tested negative for COVID-19"
			else:
				return "You do not have any results yet."
		
		
		
		tk.Frame.__init__(self, parent)
		#Go to database to get results for specific user
	
		
		userResults = tk.StringVar()
		userResults.set(results)
		label = ttk.Label(self, anchor="center",width=-100,text=updateResults(),justify=tk.CENTER,background="white",padding = 50)
		#label.grid(row = 0,columnspan = 5, padx = 10, pady = 10,sticky="ew")
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Next",
							command = lambda : controller.show_frame(Page6))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
	
	
		
#page 6 will ask the user if they want to keep going in the session
class Page6(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",width=-100,text ="Do you want\nto end the session?" ,justify=tk.CENTER,background="white",padding = 50)
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Yes",
							command = lambda : controller.show_frame(Page7))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="No",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		
#page 7 will provide the user with parting info and end the session, returning to the welcome screen
class Page7(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",width=-100,text ="Show ending info here\nand end the session" ,justify=tk.CENTER,background="white",padding = 50)
		
		label.pack(side="top",fill="x")
		

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Done",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")

#This page adds a new user to the database
#page8
class Page8(tk.Frame):
	
	def __init__(self, parent, controller):
		
		def makeUser():
			global User_first_name
			global User_last_name
			global User_DOB
			User_first_name = name_first.get()
			User_last_name = name_last.get()
			User_DOB = yearDOB.get()+"/"+monthDOB.get()+"/"+dayDOB.get()
			dbLink.addUser(User_first_name,User_last_name,User_DOB)
			controller.show_frame(Page2)
			
			
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",text="please enter your information" ,justify=tk.CENTER,background="white")
		
		label.grid(row=0,column=2,sticky=tk.E+tk.W)
		
		first_label = ttk.Label(self, anchor="w",text="First:")
		first_label.grid(row=1,column=0)
		
		#add data entry fields
		userFirstEntered = tk.StringVar()
		name_first = ttk.Entry(self,justify=tk.LEFT,textvariable=userFirstEntered)
		name_first.grid(row=1,column=1)
		
		last_label = ttk.Label(self, anchor="w",text="Last:")
		last_label.grid(row=1,column=3)
		
		userLastEntered = tk.StringVar()
		name_last = ttk.Entry(self,justify=tk.LEFT,textvariable=userLastEntered)
		name_last.grid(row=1,column=4)
		
		dob_label = ttk.Label(self, anchor="w",text="Birth Date:")
		dob_label.grid(row=3,column=0)
		
		#DOB month info
		mon_label = ttk.Label(self, anchor="center",text="mm")
		mon_label.grid(row=2,column=1)
		
		userMonthEntered = tk.StringVar()
		months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
		monthDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userMonthEntered,values = months)
		monthDOB.current(0)
		monthDOB.grid(row=3,column=1)
		
		#DOB day info
		day_label = ttk.Label(self, anchor="center",text="dd")
		day_label.grid(row=2,column=2)
		
		userDayEntered = tk.StringVar()
		days = ["01","02","03","04","05","06","07","08","09","10","11","12",
			"13","14","15","16","17","18","19","20","21","22","23","24",
			"25","26","27","28","29","30","31"]
		dayDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userDayEntered,values = days)
		dayDOB.current(0)
		dayDOB.grid(row=3,column=2)
		
		
		#DOB year info
		yr_label = ttk.Label(self, anchor="center",text="yyyy")
		yr_label.grid(row=2,column=4)
		
		userYearEntered = tk.StringVar()
		years = yearBuild.yearBuild()
		yearDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userYearEntered,values = years)
		yearDOB.current(0)
		yearDOB.grid(row=3,column=4)
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.grid(row=4,column=0,columnspan=1)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Done",
							command = makeUser)
	
		# putting the button in its place by 
		# using pack
		button2.grid(row=4,column=4,columnspan=1)

#This page will verify a person is in the system
#page 9 
class Page9(tk.Frame):
	
	def __init__(self, parent, controller):
		def updateUser(str1,str2,str3):
			global User_first_name
			global User_last_name
			global User_DOB
			

			User_first_name = str1
			User_DOB = str3
			User_last_name = str2
			return
		def searchUser():
			User_first_name = name_first.get()
			User_last_name = name_last.get()
			User_DOB = yearDOB.get()+"/"+monthDOB.get()+"/"+dayDOB.get()
			if User_DOB == "//":
				User_DOB = "1900/01/01"
			UserListed = dbLink.findUser(User_first_name,User_last_name,User_DOB)
			if UserListed == 0:
				controller.show_frame(Page10)
			elif UserListed == 1:
				
				updateUser(User_first_name,User_last_name,User_DOB)
				controller.show_frame(Page2)
				print(User_first_name + " " +User_last_name)
				
		
			else:
				controller.show_frame(StartPage)
			
			
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",text="please enter your information" ,justify=tk.CENTER,background="white")
		
		label.grid(row=0,column=2,sticky=tk.E+tk.W)
		
		first_label = ttk.Label(self, anchor="w",text="First:")
		first_label.grid(row=1,column=0)
		
		#add data entry fields
		userFirstEntered = tk.StringVar()
		name_first = ttk.Entry(self,justify=tk.LEFT,textvariable=userFirstEntered)
		name_first.grid(row=1,column=1)
		
		last_label = ttk.Label(self, anchor="w",text="Last:")
		last_label.grid(row=1,column=3)
		
		userLastEntered = tk.StringVar()
		name_last = ttk.Entry(self,justify=tk.LEFT,textvariable=userLastEntered)
		name_last.grid(row=1,column=4)
		
		dob_label = ttk.Label(self, anchor="w",text="Birth Date:")
		dob_label.grid(row=3,column=0)
		
		#DOB month info
		mon_label = ttk.Label(self, anchor="center",text="mm")
		mon_label.grid(row=2,column=1)
		
		userMonthEntered = tk.StringVar()
		months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
		monthDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userMonthEntered,values = months)
		monthDOB.current(0)
		monthDOB.grid(row=3,column=1)
		
		#DOB day info
		day_label = ttk.Label(self, anchor="center",text="dd")
		day_label.grid(row=2,column=2)
		
		userDayEntered = tk.StringVar()
		days = ["01","02","03","04","05","06","07","08","09","10","11","12",
			"13","14","15","16","17","18","19","20","21","22","23","24",
			"25","26","27","28","29","30","31"]
		dayDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userDayEntered,values = days)
		dayDOB.current(0)
		dayDOB.grid(row=3,column=2)
		
		
		#DOB year info
		yr_label = ttk.Label(self, anchor="center",text="yyyy")
		yr_label.grid(row=2,column=4)
		
		userYearEntered = tk.StringVar()
		years = yearBuild.yearBuild()
		yearDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userYearEntered,values = years)
		yearDOB.current(0)
		yearDOB.grid(row=3,column=4)
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.grid(row=4,column=0,columnspan=1)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="OK",
							command = searchUser)
	
		# putting the button in its place by 
		# using pack
		button2.grid(row=4,column=4,columnspan=1)
		
#page 10 is a rejection page for if the user doesnt exist
class Page10(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",width=-100,text ="This user\ndoes not exist" ,justify=tk.CENTER,background="white",padding = 50)
		
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Start Over",
							command = lambda : controller.show_frame(Page9))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")

		
# Driver Code
app = tkinterApp()
app.mainloop()

