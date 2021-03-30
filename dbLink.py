import mysql.connector


#The following credentials need to be updated to whereever 
#the database resides
mydb = mysql.connector.connect(
  host="localhost",
  user="Lighthouse",
  password="patients.cb2zk96gmi72.us-east-2.rds.amazonaws.com:3306",
  database="Patients"
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


	
def updateVacDate(str1,str2,str3):
	#must be yyyy/mm/dd
	mycursor = mydb.cursor()

	sql = "UPDATE information SET vaccine_date = %s WHERE first_name = %s AND last_name = %s"
	val = (str1,str2,str3)

	mycursor.execute(sql,val)

	mydb.commit()


def updateVacTime(str):
	#must be hh:mm
	mycursor = mydb.cursor()

	sql = "UPDATE information SET vaccine_time = %s WHERE first_name = %s AND last_name = %s"
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
	
if __name__ == '__main__':
	addUser()
	findUser()
	updateDOB()
	updateResults()
	updateApptDate()
	updateVacDate()
	updateApptTime()
	updateVacTime()
	getResults()
	getApptDate()
	getVacDate()
	getApptTime()
	getVacTime()
	
	

