# autoInflate.py v1.0 Beta by: Barnacules
# This script compensates for slow leaks in garbage Sleep Number beds
# that have the most garbage components known to man because they are
# $10k glorified camp beds with a fancy skin on them. Worst purchase
# of my life and new bed is on the way to replace this garbage POS
# so this script will save my back until it gets here

# Import libraries to do the actual hard work
from sleepyq import Sleepyq
from pprint import pprint
from datetime import datetime
import time
import sys

# Variables and shit
userName = '' # Enter your account login name for SleepIQ (what you login to the website with)
passWord = '' # Enter your account password
timer    = 600 # 5 minutes
pressure = 80

# Intro to feel all good and shit when I see it
print("autoInflate.py Version 1.0 Beta (By: Barnacules Nerdgasm)")
print("* This script compensates for leaky garbage $10k Sleep Number")
print("  beds that don't work for shit and nobody should ever buy one!")
print("  This script is literally saving my back right now...")
print()

# Establish connection to bed via Sleep Number website API
print("Connecting to Sleep Number Bed via sleepyQ API")
print()
client = Sleepyq(userName, passWord)
client.login()

# Output variables for easy debugging
# print("Sleepers = ", client.sleepers())
# print("Beds = ", client.beds())
# print()

# Loop until the end of time
while 1:
	# Invincable Code 101
	try:
		# Setting Bed Pressure for Left Matress
		print("+ Setting sleep number to", pressure, "at", datetime.now().strftime("%H:%M:%S"))
		client.set_sleepnumber('left', pressure, bedId='')
		
		# Sleep to let bed start to inflate a little before setting it again
		print("+ Sleeping for", timer, "seconds")
		time.sleep(timer)
	except:		
		print("- Oops, something fucked up... It'll be fine though...")
		try:
			client = Sleepyq(userName, passWord)
			client.login()
		except:
			print("- failed to connect to bed, waiting 60 seconds to retry")
			time.sleep(60)
		
		# Sleep for 5 seconds giving time for double CTRL-C to exit program
		time.sleep(60)
		pass
	else:
		print("+ Everything worked as planned, let's do it again")
