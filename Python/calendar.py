import calendar
from datetime import date
from datetime import datetime

# handling user exceptions
try:
	year = int( input("Enter the year of the required calendar\n"))
	month = int( input("Enter the month of the required calendar\n"))

	# getting current date and time with their proper formatting
	today = date.today()
	today_formatted = today.strftime("%d/%m/%Y")
	current_time = datetime.now().strftime("%H:%M:%S")

	# splitting all parts of the time in a list because from there we can get the idea of PM OR AM.
	current_time_list = current_time.split(":")

	# checking for the conditions of AM OR PM
	if(int(current_time_list[0])>=24):
		current_time += " AM"
	elif(int(current_time_list[0])>=12):
		current_time += " PM"


	print(f"Current Time : {current_time}\nToday is {today_formatted}\n-------------------")
	print(calendar.month(year,month)) 


except Exception as e:
	print("Please make sure your input is in correct format.")
