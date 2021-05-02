import mysql.connector
import numpy


#The following credentials need to be updated to whereever 
#the database resides
mydb = mysql.connector.connect(
  host="lighthouse.digital.uic.edu",
  user="lighthou_team",
  password="SeniorDesign2",
  database="lighthou_patients"
)

def addUser(str1,str2,str3):
	mycursor = mydb.cursor()

	sql = "INSERT INTO information (first_name, last_name, DOB) VALUES (%s,%s,%s)"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

def findUser(str1,str2,str3):
	mycursor = mydb.cursor()

	sql = "SELECT EXISTS (SELECT * FROM information WHERE first_name = %s AND last_name = %s AND DOB = %s)"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	return record[0]

def updateDOB(str1,str2,str3):
	#must be yyyy/mm/dd
	mycursor = mydb.cursor()

	sql = "UPDATE information SET DOB = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

def updatePhone(str1,str2,str3):
	
	mycursor = mydb.cursor()

	sql = "UPDATE information SET phone = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

def updateApptDate(str1,str2,str3):
	#must be yyyy/mm/dd
	mycursor = mydb.cursor()

	sql = "UPDATE information SET appointment_date = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()


	
def updateApptTime(str1,str2,str3):
	#must be hh:mm
	mycursor = mydb.cursor()

	sql = "UPDATE information SET appointment_time = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

def updateApptLoc(str1,str2,str3):
	#must be hh:mm
	mycursor = mydb.cursor()

	sql = "UPDATE information SET appointment_location = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

	
def updateVacDate(str1,str2,str3):
	#must be yyyy/mm/dd
	mycursor = mydb.cursor()

	sql = "UPDATE information SET vaccine_date = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()


def updateVacTime(str1,str2,str3):
	#must be hh:mm
	mycursor = mydb.cursor()

	sql = "UPDATE information SET vaccine_time = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()
	
def updateVacLoc(str1,str2,str3):
	#must be hh:mm
	mycursor = mydb.cursor()

	sql = "UPDATE information SET vaccine_location = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

	
	
def updateResults(str1,str2,str3):
	mycursor = mydb.cursor()

	sql = "UPDATE information SET HasCovid = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()

	
	
def getResults(str1,str2):
	mycursor = mydb.cursor()

	sql = "SELECT HasCovid FROM information WHERE first_name = %s AND last_name = %s"
	val = (str1,str2)

	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	if record is None:
		return "N/A"
	
	result = record[0]

	return result
	
def getApptDate(str1,str2):
	mycursor = mydb.cursor()

	sql = "SELECT appointment_date FROM information WHERE first_name = %s AND last_name = %s"
	val = (str1,str2)

	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	date = record[0]
	return date
	
def getVacDate(str1,str2):
	mycursor = mydb.cursor()

	sql = "SELECT vaccine_date FROM information WHERE first_name = %s AND last_name = %s"
	val = (str1,str2)

	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	date = record[0]
	return date
	
def getApptTime(str1,str2):
	mycursor = mydb.cursor()
	
	sql = "SELECT appointment_time FROM information WHERE first_name = %s AND last_name = %s"
	val = (str1,str2)
	
	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	timeRaw = record[0]
	time = str(timeRaw)
	
	return time
	
def getVacTime(str1,str2):
	mycursor = mydb.cursor()
	
	sql = "SELECT vaccine_time FROM information WHERE first_name = %s AND last_name = %s"
	val = (str1,str2)
	
	mycursor.execute(sql,val)
	record = mycursor.fetchone()
	
	timeRaw = record[0]
	time = str(timeRaw)
	
	return time

def createApptEntry(str1,str2,str3):
	mycursor = mydb.cursor()

	sql = "INSERT INTO "+str3+" (Location,Date) VALUES (%s,%s)"
	val = (str1,str2)

	mycursor.execute(sql,val)

	mydb.commit()
	
def createApptTable(str1):
	mycursor = mydb.cursor()

	sql = "CREATE TABLE "+str1+" (Location varchar(30), Date varchar(20), `s11:00` varchar(12), `s11:15` varchar(12), `s11:30` varchar(12), `s11:45` varchar(12), `s12:00` varchar(12), `s12:15` varchar(12), `s12:30` varchar(12), `s12:45` varchar(12), `s01:00` varchar(12), `s01:15` varchar(12), `s01:30` varchar(12), `s01:45` varchar(12), `s02:00` varchar(12), `s02:15` varchar(12), `s02:30` varchar(12), `s02:45` varchar(12));"
	

	mycursor.execute(sql)

	mydb.commit()
def createInfoTable(str1):
	mycursor = mydb.cursor()

	sql = "CREATE TABLE "+str1+" (first_name varchar(30), last_name varchar(30), DOB varchar(20), phone varchar(12), appointment_date varchar(12), appointment_time varchar(12), appointment_location varchar(30), vaccine_date varchar(12), vaccine_time varchar(12), vaccine_location varchar(30), HasCovid varchar(4));"
	

	mycursor.execute(sql)

	mydb.commit()
	
def updateSchedule(str1,str2,str3,str4,str5):
	#must be hh:mm
	mycursor = mydb.cursor()

	#since column names in database contain colons backticks(``) are needed to reference them
	sql = "UPDATE "+str1+" SET `s"+str2+"` = %s WHERE (Date = %s) AND (Location = %s)"
	val = (str3,str4,str5)

	mycursor.execute(sql,val)

	mydb.commit()
	
def getScheduleTimes(str1,str2,str3):
	if str3 == "" or str2 == "" or str2 == "What Site?":
		return "none"
	else:
		mycursor = mydb.cursor()
	
		sql = "SELECT * FROM "+str1+" WHERE Location = %s AND Date = %s"
		val = (str2,str3)
	
		mycursor.execute(sql,val)
		record = mycursor.fetchone()
	
		i=0
		timesAvail = []
		for t in record:
			if t != "":
				timesAvail.append(str(t))
				i+=1
		
		timesAvail.pop(0)
		timesAvail.pop(0)
		
		if len(timesAvail) == 0:
			timesAvail.append("none")
		else:
			timesAvail.insert(0,str(i-2)+" time(s) available")
		return timesAvail
	
if __name__ == '__main__':
	addUser()
	findUser()
	updateDOB()
	updatePhone()
	updateResults()
	updateApptDate()
	updateVacDate()
	updateApptTime()
	updateVacTime()
	updateApptLoc()
	updateVacLoc()
	getResults()
	getApptDate()
	getVacDate()
	getApptTime()
	getVacTime()
	createApptEntry()
	updateSchedule()
	getScheduleTimes()
	createApptTable()

