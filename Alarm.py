import time


print("Welcome User \nCreated by:- Simarjot Singh")
def myAlarm():
	try:
		myTime = list(map(int, input("Enter in hh mm ss format: ").split()))
		if len(myTime) == 3:
			total = myTime[0]*3600 + myTime[1]*60 + myTime[2]
			time.sleep(total)
			for i in range(10):
		                print('\a')
                		time.sleep(1)
			
		else:
			print("Invalid Format!")
			myAlarm()
	except Exception as e:
		print("Exception: ",e)
		myAlarm()



myAlarm()
