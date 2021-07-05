
'''
a bot plan sending sceduals - weekly reminders

another idea is to make a command with all current program going
it opens a notepad

Perfect version of it:
	You type the name of the event and the date then 
		it adds it to a notepad and sceduals a time for it
		everyweek it reminds you an hour before,

	There is a command to give you all the current events going by opening a file
	You can make a command to see how many days until Ramadan
--------------------------
Part one: takes the name of the program and adds it to a cmd == DONE 
	Part two: Takes emojies on the message if you want to sceduale it, click the clock, if not click X (EXTRA)

Part three: takes time and make a weekly reocuring message (the main bot - this first)
	Step 1: Make the bot send weekly Friday reminders (the main point of it)
	Step 2: After you get a reoccuing method, you then can make a way to input other commands from users
	Step 3: merge the method with the CMD
	Step 4: add emojies to messages (here after you learn on emjies you can add also add a command to like and dislike on feedback channel for MSA)
	
EXTRA:
	Step 5: maybe tell the user what time is it when he asks
import asyncio
import datetime
import pytz

MessageTime =  datetime.date(2021,1,18)

#tday = datetime.date.today() #prints the date of today
#if (MessageTime==tday):
#	print (tday)
#print (datetime.datetime.now())

#try to send a certain message on a certain minute using if ==
#make that 

#the last step is testing it on discord '''
import datetime
import asyncio

import pytz
#usertime = input("enter time") leave this till the end for now we want to get the bot running
#check if the same month then same day then same hour then same minute for minute you just

 #the time in 24 hrs | (year, month, day, hrs, min, sec, microsecond)


#the_time = now.time().hour
#print (now.month)

#just try make it send a message "jumaa mubarakah, don't for get to read surat alkahf" for now

def everyFriday(): #switches to this week's Friday
	now=datetime.datetime.now()
	week= datetime.timedelta(days = 7)
	thisWeeksFriday=datetime.datetime(2021,1,1,6,0)#do NOT change these numbers! this is one friday

	while (thisWeeksFriday < now):
		try:
			thisWeeksFriday += week 
			#print (thisWeeksFriday, "1")
			if (thisWeeksFriday >= now):
				return thisWeeksFriday
		except:
			print ("everyFriday broke")
			pass

	
#print (everyFriday().day)
		#multiple = True

		#store time data in UTC (int) constant time check every 2 min 
		#when it matches the time you take that line and notifie people
		#

async def timeloop():
	i = 0
	remindMeAT =datetime.datetime(2021,5,1,22,5)#year,month,day,hour,min,sec 
												# it is a custom day and time you want to be reminded at

	#/start reminder 

	#make an if statement for remindMeAt
	#i can make an if statement if now is smaller than remind me at then increase the date by ** so we get reminders and I only do it once
	#or you can make if it is a multiple of 7 by taking the remainder using this notation //
	
	tdelta = datetime.timedelta(minutes = 2) #the loop every () the message will be sent after the remindmeAt heppens
	while True:
		now=datetime.datetime.now() #has to be in the loop to renew the time
		print (now)
		#print (everyFriday())
		try:
			if (remindMeAT.day==now.day and remindMeAT.hour==now.hour and remindMeAT.minute==now.minute):#same day and?
				print("it is the same day")
				remindMeAT = (remindMeAT+tdelta) # it should send a message every two minutes
				await asyncio.sleep (31)
			
			if (everyFriday().day==now.day and everyFriday().hour==now.hour and everyFriday().minute==now.minute):
				print("jumaa mubarakah :) \ndon't foget to:\n 1:read surat alkahf\n 2:make dua")
			
			else:
				await asyncio.sleep(1) #I have a propblem here, I want it to go back to the main function when it does not find the time
		except:
			print ("broke")
			break

loop = asyncio.get_event_loop()


try : #loop that runs it forever
	asyncio.ensure_future(timeloop())
	#asyncio.ensure_future(everyFriday())
	loop.run_forever()
except KeyboardInterrupt:
	pass
finally:
	print ("closing loop")
	loop.close()


#tasks convert the time for it to be in eastern time
#you will need an if for the day (will be 12 hours which is 43200 seconds) and an if for the hour (acyncio will be 30 min which is 1800 seconds)
#always make sure to put the seconds meaning the seconds so convert the time outside the code