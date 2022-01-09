
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