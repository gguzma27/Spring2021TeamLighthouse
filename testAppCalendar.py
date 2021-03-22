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

from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk


#This font was used early in the script can be used again
#just haven't really looked at it

LARGEFONT =("Verdana", 35)


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
		for F in (StartPage, Page1, Page2,Page3,Page4,Page5,Page6,Page7):

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
		label = ttk.Label(self, anchor="center",width=-100,text ="This is where\nwe verify users" ,justify=tk.CENTER,background="white",padding = 50)
		
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
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using pack
		button2.pack(side="right")



# third window frame page2
# our main menu
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="n",text ="Main Menu",width=-80, justify=tk.CENTER)
		label.grid(row = 0,column = 1,columnspan=3, padx = 10, pady = 10,sticky="ew")
		
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Schedule Test",command = lambda : controller.show_frame(Page3))
	
							
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 0, ipadx = 40, ipady = 10)
	
		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Schedule Vaccine",command = lambda : controller.show_frame(Page4))
		
							
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 2, ipadx = 40, ipady = 10)
			
		
		button3 = ttk.Button(self,text="See Results", command = lambda : controller.show_frame(Page5))
		button3.grid(row = 1, column = 4, ipadx = 40, ipady = 10)
	

#page 3 is where we will schedule appts
class Page3(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#label = ttk.Label(self, anchor="center",width=-100,text ="This is where\nwe #schedule appointments" ,justify=tk.CENTER,background="white",padding = 50)
		#label.grid(row = 0,columnspan = 5, padx = 10, pady = 10,sticky="ew")
		#label.pack(side="top",fill="x")
		
		cal = Calendar(self, selectmode='none')
		date = cal.datetime.today() + cal.timedelta(days=2)
		cal.calevent_create(date, 'Hello World', 'message')
		cal.calevent_create(date, 'Reminder 2', 'reminder')
		cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
		cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
		cal.tag_config('reminder', background='red', foreground='yellow')
		cal.pack(fill="both", expand=True)
		
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
		tk.Frame.__init__(self, parent)
		#label = ttk.Label(self, anchor="center",width=-100,text ="This is where\nwe #schedule vaccines" ,justify=tk.CENTER,background="white",padding = 50)
		#label.pack(side="top",fill="x")
		
		cal = Calendar(self, selectmode='none')
		date = cal.datetime.today() + cal.timedelta(days=2)
		cal.calevent_create(date, 'Hello World', 'message')
		cal.calevent_create(date, 'Reminder 2', 'reminder')
		cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
		cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
		cal.tag_config('reminder', background='red', foreground='yellow')
		cal.pack(fill="both", expand=True)
		
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
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, anchor="center",width=-100,text ="This is where\nwe see results" ,justify=tk.CENTER,background="white",padding = 50)
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
		
# Driver Code
app = tkinterApp()

app.mainloop()

