'''
This setup program assumes that a database exists 
and has a connection to said database. This program only 
sets up the tables for the database, not the database itself
-Glenn Guzman-Rockett 
'''
import dbLink

monthCorrect = False
Finished = False

month_dict = {
    0: 'No month',
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

times = {"11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","01:00","01:15","01:30","01:45","02:00","02:15","02:30","02:45"}
locations = {"Location1", "Location2"}
tables = {"apptSchedule","vaccineSchedule"}
while not Finished:
	while not monthCorrect:
		month = input("What month do the appointments need to cover(1-12)?:")
		if int(month)>=1 and int(month)<=12:
			monthCorrect = True
		print("You entered ", month_dict[int(month)])


	isCorrect = input("Is this correct(y/n)?:")


	if isCorrect == 'y' or isCorrect == 'Y':
		if int(month) < 10:
			monthNum = "0"+str(int(month))
		else:
			monthNum = str(int(month))
		dbLink.createInfoTable("information")
	
		dbLink.createApptTable("apptSchedule")
		dbLink.createApptTable("vaccineSchedule")
	
		if int(month) == 2:
			i = 28
		elif int(month) == 9 or int(month) == 6 or int(month) == 4 or int(month) == 11:
			i = 30
		else:
			i = 31
		
		while i > 0:
			if i>9:
				day = str(i)
			else:
				day = "0"+str(i)
				
			date = "2021/"+monthNum+"/"+day
			for T in tables:
				for L in locations:
					dbLink.createApptEntry(L,date,T)
					for A in times:
						dbLink.updateSchedule(T,A,A,date,L)
			i -=1
			print(str(i) + " dates left")
		Finished = True 
	else:
		print("Please input the correct month")
		monthCorrect = False
		Finished = False

