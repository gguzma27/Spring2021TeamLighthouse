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

LARGEFONT =("Verdana", 16)

global User_first_name
global User_last_name
global User_DOB
global results
global vacDay
global vacTime
global apptDay
global apptTime
global vacLoc
global apptLoc

results = ""
User_first_name = ""
User_DOB = ""
User_last_name = ""
vacDay = ""
vacTime = ""
apptDay = ""
apptTime = ""
vacLoc = ""
apptLoc = ""


class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self,bg="#000000") 
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
		for F in (StartPage, Page1, Page2,Page3,Page4,Page5,Page6,Page7,Page8,Page9,Page10,Page11,Page12):

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
	def get_page(self, classname):
        #Returns an instance of a page given it's class name as a string'''
        	for page in self.frames.values():
            		if str(page.__class__.__name__) == classname:
                		return page
        	return None
	def update(self):
		global results
		global apptDay
		global apptTime
		global vacDay
		global vacTime
		global vacLoc
		global apptLoc
		
		page3=self.get_page("Page3")
		available = dbLink.getScheduleTimes("apptSchedule",apptLoc,apptDay)
		page3.cb1.configure(values=available)
		page3.cb1.current(0)
		
		page4=self.get_page("Page4")
		available = dbLink.getScheduleTimes("vaccineSchedule",vacLoc,vacDay)
		page4.cb1.configure(values=available)
		page4.cb1.current(0)
		
		
		page11= self.get_page("Page11")
		if apptDay == "" or apptTime == "":
			confirm1 = "You have not scheduled an appointment. Would you like to proceed?"
		else:
			confirm1 = "Would you like to confirm your appointment on "+apptDay+" at "+apptTime
		page11.label.configure(text=str(confirm1))
		
		page12= self.get_page("Page12")
		if vacDay == "" or vacTime == "":
			confirm2 = "You have not scheduled an appointment. Would you like to proceed?"
		else:
			confirm2 = "Would you like to confirm your appointment on "+vacDay+" at "+vacTime
		page12.label.configure(text=str(confirm2))
		
		
		page5 = self.get_page("Page5")
			
		if results == "yes":
			msg = "You have tested positive for COVID-19"
		elif results == "no":
			msg = "You have tested negative for COVID-19"
		else:
			msg = "You do not have any results yet."
			
		page5.label.configure(text=str(msg))
		app.after(500,self.update)
	
# first window frame startpage, this will be the welcome page
class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.logo=ImageTk.PhotoImage(Image.open("images/OSFLogo.png"))
		
		# label of frame Layout 2
		label = tk.Label(self, image=self.logo,anchor="center",compound = tk.TOP,width=-100,text ="Welcome to OSF Healthcare!",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx = 20)#,font = LARGEFONT)
		
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		
		#Used a White background to get a sense of the space of the label
		
		# putting the label in its place by using
		# using pack
		label.pack(side="top",fill="x")
		
		button1 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="Click Here\nto Begin",compound="center",command = lambda : controller.show_frame(Page1))
		
	
		# putting the button in its place by
		# using pack
		button1.pack(side="bottom")




# second window frame page1, our verfication page
# this will be a pass through for now: 03/22/2021 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		
		label = tk.Label(self, anchor="center",width=-100,text ="Are you a\nnew user?" ,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx = 50,pady=50)
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="Yes",compound="center",command = lambda : controller.show_frame(Page8))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="No",compound="center",command = lambda : controller.show_frame(Page9))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")




# third window frame page2
# our main menu

class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		def findResults():
			global results
			global User_first_name
			global User_last_name
			results = dbLink.getResults(User_first_name,User_last_name)
			print(User_first_name + " " +User_last_name+" "+str(results))
			controller.show_frame(Page5)
		
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		#added icons for Menu Buttons
		self.my_img = ImageTk.PhotoImage(Image.open("images/calendar1.png"))
		self.resultsImg = ImageTk.PhotoImage(Image.open("images/resultsAdj.png"))

		
		label = tk.Label(self, anchor="n",text ="Main Menu",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,width=-80, justify=tk.CENTER)
		label.grid(row = 0,column = 1,columnspan=3, padx = 10, pady = 10,sticky="ew")
		
		
		# button to show frame 2 with text
		# layout2ff",c
		button1 = tk.Button(self,image=self.my_img,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,compound = tk.BOTTOM,text ="Schedule Test",command = lambda : controller.show_frame(Page3))
	
							
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 0, ipadx = 10, ipady = 10)
	
		# button to show frame 3 with text
		# layout3
		button2 = tk.Button(self,image=self.my_img,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,compound = tk.BOTTOM, text ="Schedule Vaccine",command = lambda : controller.show_frame(Page4))
		
							
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 2, ipadx = 10, ipady = 10)
			
		
		button3 = tk.Button(self,image=self.resultsImg,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0, compound = tk.BOTTOM, text="See Results", command = findResults)
		button3.grid(row = 1, column = 4, ipadx = 10, ipady = 5)
		
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 1)
		self.grid_columnconfigure(2, weight = 1)
		self.grid_columnconfigure(3, weight = 1)
		self.grid_columnconfigure(4, weight = 1)
		

#page 3 is where we will schedule appts
class Page3(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		#assignment functions to make variables out of user selection
		def date_assign(e):
			global apptDay
			apptDay = str(self.cal.get_date())
			return
		
		def time_assign(e):
			global apptTime
			apptTime = str(self.cb1.get())
			return
			
		def loc_assign(e):
			global apptLoc
			apptLoc = str(self.cb2.get())
			return
			
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		#Calendar section, set to day selection
		self.cal = Calendar(self, selectmode='day', date_pattern = 'y/mm/dd')
		self.cal.pack(fill="both", expand=True)
		
		
		#Time Slot section
		self.var1 = tk.StringVar()
		self.var2 = tk.StringVar()
		options = ["none"]
		places = ["What Site?","Location1","Location2"]
		self.cb1 = ttk.Combobox(self, textvariable=self.var1, values=options)
		self.cb2 = ttk.Combobox(self, textvariable=self.var2, values=places)
		self.cb1.current(0)
		self.cb2.current(0)

		#both the calender and combobox are bound to selection events
		self.cal.bind("<<CalendarSelected>>",date_assign)
		self.cb1.bind("<<ComboboxSelected>>",time_assign)
		self.cb2.bind("<<ComboboxSelected>>",loc_assign)
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="StartPage",image=self.button1,bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")
		self.cb1.pack(side="left")
		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self, text ="Next",image=self.button1,bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = lambda : controller.show_frame(Page11))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		self.cb2.pack(side="right")
#page 4 is where we will schedule vaccines
class Page4(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		#assignment functions to make variables out of user selection
		def date_assign(e):
			global vacDay
			vacDay = str(self.cal.get_date())
			return
		
		def time_assign(e):
			global vacTime
			vacTime = str(self.cb1.get())
			return
			
		def loc_assign(e):
			global vacLoc
			vacLoc = str(self.cb2.get())
			return
			
	
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		#Calendar section, set to day selection
		self.cal = Calendar(self, selectmode='day', date_pattern = 'y/mm/dd')
		self.cal.pack(fill="both", expand=True)
		
		
		#Time Slot section
		self.var1 = tk.StringVar()
		self.var2 = tk.StringVar()
		options = ["none"]
		places = ["What Site?","Location1","Location2"]
		self.cb1 = ttk.Combobox(self, textvariable=self.var1, values=options)
		self.cb2 = ttk.Combobox(self, textvariable=self.var2, values=places)
		self.cb1.current(0)
		self.cb2.current(0)

		#both the calender and combobox are bound to selection events
		self.cal.bind("<<CalendarSelected>>",date_assign)
		self.cb1.bind("<<ComboboxSelected>>",time_assign)
		self.cb2.bind("<<ComboboxSelected>>",loc_assign)
		
		
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="StartPage",image=self.button1,bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")
		self.cb1.pack(side="left")
		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self, text ="Next",image=self.button1,bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = lambda : controller.show_frame(Page12))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		self.cb2.pack(side="right")
		
#page 5 is where we will see results
class Page5(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		#Go to database to get results for specific user
		
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
	
		
		userResults = tk.StringVar()
		userResults.set(results)
		self.label = tk.Label(self, anchor="center",width=-100,text="dunno",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx= 50,pady=50)
		self.label.pack(side="top",fill="x")
		

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,image=self.button1,compound="center", text ="Next",bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(Page6))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
	
	
		
#page 6 will ask the user if they want to keep going in the session
class Page6(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		label = tk.Label(self, anchor="center",width=-100,text ="Do you want\nto end the session?" ,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx= 50,pady=50)
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="Yes",compound="center",image = self.button1,bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(Page7))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self, text ="No",compound="center",image = self.button1,bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		
#page 7 will provide the user with parting info and end the session, returning to the welcome screen
class Page7(tk.Frame): 
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.endPic = ImageTk.PhotoImage(Image.open("images/EndPic.png"))
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		
		label = tk.Label(self, image=self.endPic,anchor="center",width=-100,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx = 20,pady=15)
		
		label.pack(side="top",fill="x")
		

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self, image=self.button1,compound="center",text ="Done",bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")

#This page adds a new user to the database
#page8
class Page8(tk.Frame):
	
	def __init__(self, parent, controller):
		self.controller = controller
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
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		label = tk.Label(self, anchor="center",text="please enter your information" ,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER)
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 1)
		self.grid_columnconfigure(2, weight = 1)
		self.grid_columnconfigure(3, weight = 1)
		self.grid_columnconfigure(4, weight = 1)
		self.grid_rowconfigure(3, weight = 2)
		self.grid_rowconfigure(4, weight = 1)
		label.grid(row=0,column=2,sticky=tk.E+tk.W)
		
		first_label = tk.Label(self, anchor="w",text="First:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		first_label.grid(row=1,column=0)
		
		#add data entry fields
		userFirstEntered = tk.StringVar()
		name_first = tk.Entry(self,justify=tk.LEFT,textvariable=userFirstEntered)
		name_first.grid(row=1,column=1)
		
		last_label = tk.Label(self, anchor="w",text="Last:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		last_label.grid(row=1,column=3)
		
		userLastEntered = tk.StringVar()
		name_last = tk.Entry(self,justify=tk.LEFT,textvariable=userLastEntered)
		name_last.grid(row=1,column=4)
		
		dob_label = tk.Label(self, anchor="w",text="Birth Date:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		dob_label.grid(row=3,column=0)
		
		#DOB month info
		mon_label = tk.Label(self, anchor="center",text="mm",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		mon_label.grid(row=2,column=1)
		
		userMonthEntered = tk.StringVar()
		months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
		monthDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userMonthEntered,values = months)
		monthDOB.current(0)
		monthDOB.grid(row=3,column=1)
		
		#DOB day info
		day_label = tk.Label(self, anchor="center",text="dd",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		day_label.grid(row=2,column=2)
		
		userDayEntered = tk.StringVar()
		days = ["01","02","03","04","05","06","07","08","09","10","11","12",
			"13","14","15","16","17","18","19","20","21","22","23","24",
			"25","26","27","28","29","30","31"]
		dayDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userDayEntered,values = days)
		dayDOB.current(0)
		dayDOB.grid(row=3,column=2)
		
		
		#DOB year info
		yr_label = tk.Label(self, anchor="center",text="yyyy",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		yr_label.grid(row=2,column=4)
		
		userYearEntered = tk.StringVar()
		years = yearBuild.yearBuild()
		yearDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userYearEntered,values = years)
		yearDOB.current(0)
		yearDOB.grid(row=3,column=4)
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self,image=self.button1, text ="StartPage",compound="center",bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.grid(row=4,column=0,columnspan=1)

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,image=self.button1, text ="Done",compound="center",bd=0,bg="#000000",highlightthickness=0,
							command = makeUser)
	
		# putting the button in its place by 
		# using pack
		button2.grid(row=4,column=4,columnspan=1)

#This page will verify a person is in the system
#page 9 
class Page9(tk.Frame):
	
	def __init__(self, parent, controller):
		self.controller = controller
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
			
			name_first.delete(0,last=tk.END)
			name_last.delete(0,last=tk.END)
			yearDOB.delete(0,last=tk.END)
			monthDOB.delete(0,last=tk.END)
			dayDOB.delete(0,last=tk.END)
			
			
			if User_DOB == "//":
				User_DOB = "1900/01/01"
			UserListed = dbLink.findUser(User_first_name,User_last_name,User_DOB)
			if UserListed == 0:
				controller.show_frame(Page10)
				
			elif UserListed == 1:
				
				updateUser(User_first_name,User_last_name,User_DOB)
				controller.show_frame(Page2)
				#print(User_first_name + " " +User_last_name)
				
		
			else:
				controller.show_frame(StartPage)
			
			
		tk.Frame.__init__(self, parent)
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 1)
		self.grid_columnconfigure(2, weight = 1)
		self.grid_columnconfigure(3, weight = 1)
		self.grid_columnconfigure(4, weight = 1)
		self.grid_rowconfigure(3, weight = 2)
		self.grid_rowconfigure(4, weight = 1)
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		label = tk.Label(self, anchor="center",text="please enter your information" ,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,pady=25)
		
		label.grid(row=0,column=2,sticky=tk.E+tk.W)
		
		first_label = tk.Label(self, anchor=tk.W,text="First:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		first_label.grid(row=1,column=1)
		
		#add data entry fields
		userFirstEntered = tk.StringVar()
		name_first = tk.Entry(self,justify=tk.LEFT,textvariable=userFirstEntered)
		name_first.grid(row=2,column=1)
		
		last_label = tk.Label(self, anchor="w",text="Last:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		last_label.grid(row=1,column=3)
		
		userLastEntered = tk.StringVar()
		name_last = tk.Entry(self,justify=tk.LEFT,textvariable=userLastEntered)
		name_last.grid(row=2,column=3)
		
		dob_label = tk.Label(self, anchor="w",text="Birth Date:",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		dob_label.grid(row=4,column=0)
		
		#DOB month info
		mon_label = tk.Label(self, anchor="center",text="mm",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		mon_label.grid(row=3,column=1)
		
		userMonthEntered = tk.StringVar()
		months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
		monthDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userMonthEntered,values = months)
		monthDOB.current(0)
		monthDOB.grid(row=4,column=1)
		
		#DOB day info
		day_label = tk.Label(self, anchor="center",text="dd",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		day_label.grid(row=3,column=2)
		
		userDayEntered = tk.StringVar()
		days = ["01","02","03","04","05","06","07","08","09","10","11","12",
			"13","14","15","16","17","18","19","20","21","22","23","24",
			"25","26","27","28","29","30","31"]
		dayDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userDayEntered,values = days)
		dayDOB.current(0)
		dayDOB.grid(row=4,column=2)
		
		
		#DOB year info
		yr_label = tk.Label(self, anchor="center",text="yyyy",bd=0,bg="#000000",fg="#ffffff",highlightthickness=0)
		yr_label.grid(row=3,column=3)
		
		userYearEntered = tk.StringVar()
		years = yearBuild.yearBuild()
		yearDOB = ttk.Combobox(self,justify=tk.LEFT,textvariable=userYearEntered,values = years)
		yearDOB.current(0)
		yearDOB.grid(row=4,column=3)
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self,image=self.button1, text ="StartPage",compound="center",bd=0,bg="#000000",highlightthickness=0,
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.grid(row=5,column=0,sticky="SW")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,image=self.button1, text ="OK",compound="center",bd=0,bg="#000000",highlightthickness=0,
							command = searchUser)
	
		# putting the button in its place by 
		# using pack
		button2.grid(row=5,column=4,sticky="SE")
		
#page 10 is a rejection page for if the user doesnt exist
class Page10(tk.Frame):
	
	def __init__(self, parent, controller):
		def updateUser(str1,str2,str3):
			global User_first_name
			global User_last_name
			global User_DOB
			

			User_first_name = str1
			User_DOB = str3
			User_last_name = str2
			return
		def startOver():
			updateUser("","","")
			controller.show_frame(Page9)
			
			
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		label = tk.Label(self, anchor="center",width=-100,text ="This user\ndoes not exist" ,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx= 50,pady=50)
		
		label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, image=self.button1,text ="StartPage",bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,image=self.button1, text ="Start Over",bd=0,bg="#000000",highlightthickness=0,compound="center",
							command = startOver)
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")

# Page 11: Appt Confirmation Page
# this window acts as an appt confimation page
class Page11(tk.Frame):
	
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		
		def updateApptRecords():
			global apptDay
			global apptTime
			global User_first_name
			global User_last_name 
			
			if apptDay == "" or apptTime == "":
				controller.show_frame(Page6)
			else:
				dbLink.updateApptDate(apptDay,User_first_name,User_last_name)
				dbLink.updateApptTime(apptTime,User_first_name,User_last_name)
				controller.show_frame(Page6)
			
			
		global apptDay
		global apptTime
		confirmMsg = "something"
		
		self.label = tk.Label(self, anchor="center",width=-100,text =confirmMsg,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx = 50,pady=40,wraplength=400)
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		self.label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="Yes",compound="center",command = updateApptRecords)
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="No",compound="center",command = lambda : controller.show_frame(Page3))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")
		
# Page 12: Vaccine Confirmation Page
# this window acts as an appt confimation page
class Page12(tk.Frame):
	
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.configure(bg="#000000")
		
		def updateVacRecords():
			global vacDay
			global vacTime
			global vacLoc
			global User_first_name
			global User_last_name 
			
			if vacDay == "" or vacTime == "":
				controller.show_frame(Page6)
			else:
				dbLink.updateVacDate(vacDay,User_first_name,User_last_name)
				dbLink.updateVacTime(vacTime,User_first_name,User_last_name)
				dbLink.updateVacLoc(vacLoc,User_first_name,User_last_name)
				dbLink.updateSchedule("vaccineSchedule",vacTime,"",vacDay,vacLoc)
				controller.show_frame(Page6)
			
			
		
		
		global vacDay
		global vacTime
		confirmMsg = "something"
		
		self.label = tk.Label(self, anchor="center",width=-100,text =confirmMsg,bd=0,bg="#000000",fg="#ffffff",highlightthickness=0,justify=tk.CENTER,padx = 50,pady=40,wraplength=400)
		self.button1 = ImageTk.PhotoImage(Image.open("images/greybutton.png"))
		self.label.pack(side="top",fill="x")
		
		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="Yes",compound="center",command = updateVacRecords)
	
		# putting the button in its place 
		# by using pack
		button1.pack(side="left")

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self,bg="#000000", image=self.button1, border = 0,bd = 0,highlightthickness=0,text ="No",compound="center",command = lambda : controller.show_frame(Page4))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")



		
# Driver Code
app = tkinterApp()
app.title("OSF HealthCare")
app.after(500,app.update())
app.mainloop()

