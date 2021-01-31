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

try:
	y = int(input("Enter number to test: "))
	if (y < 0):
		raise ValueError()
except ValueError:
		print("Input is not an positive integer.")
else:
	if (isLeapYear(y)):
		print("{} is a leap year.".format(y))
	else:
		print("{} is not a leap year.".format(y))
finally:
	input("Press ENTER to exit")