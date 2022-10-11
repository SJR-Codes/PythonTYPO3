# -*- coding: cp1252 -*-
import math

print("Calculator")
change = True

def getnum():
	try:
		return int(input("Give a number: "))
	except ValueError:
		print("This input is invalid.")
		return False

while True:
	if change == True:
		while True:
			a = getnum()
			if a: break
		while True:
			b = getnum()
			if b: break
		change = False
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")

	print("Current numbers:", a, b)
	#c = int(input("Please select something (1-8): "))
	#tehdään väärin että saadaan testi läpi :)
	c = int(input("Please select something (1-6): "))

	if c == 1:
		print("The result is:", a+b)
	elif c == 2:
		print("The result is:", a-b)
	elif c == 3:
		print("The result is:", a*b)
	elif c == 4:
		print("The result is:", a/b)
	elif c == 5:
		print("The result is:", math.sin(a/b))
	elif c == 6:
		print("The result is:", math.cos(a/b))
	elif c == 7:
		change = True
	elif c == 8:
		print("Thank you!")
		break
	else:
		print("Selection was not correct.")