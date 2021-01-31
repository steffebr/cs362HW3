# To run the program in windows, simply double click the file Steffen325HW1.py and follow the console prompts

import math

def isLeapYear(x):
	if (x % 4 != 0):
		return False
	elif (x % 100 != 0):
		return True
	elif (x % 400 != 0):
		return False
	else:
		return True
			
		
	
y = int(input("Enter number to test: "))

if (isLeapYear(y)):
	print("{} is a leap year.".format(y))
else:
	print("{} is not a leap year.".format(y))
input("Press ENTER to exit")