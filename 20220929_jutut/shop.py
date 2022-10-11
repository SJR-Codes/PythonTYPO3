# -*- coding: cp1252 -*-

cart = []

while True:
	try:
		sel = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: "))
	except ValueError:
		print("Invalid value!")
		continue
	if sel == 1:
		cart.append(input("What will be added? "))
	elif sel == 2:
		print(f"There are {len(cart)} items in the list.")
		d = int(input("Which item is deleted?: "))
		try:
			cart.pop(d)
		except IndexError:
			print("Incorrect selection.")
	elif sel == 3:
		print("The following items remain in the list:")
		for i in cart:
			print(i)
		break
	else:
		print("Incorrect selection.")
