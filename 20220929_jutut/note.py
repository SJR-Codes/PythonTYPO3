# -*- coding: cp1252 -*-
import time

filen = "notebook.txt"

try:
	fh = open(filen, "r")
except IOError:
	fh = open(filen, "w")
	fh.close()
	print("No default notebook was found, created one.")

while True:
	print(f"Now using file {filen}")
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit")
	sel = int(input("Please select one: "))
	
	if sel == 1:
		fh = open(filen, "r")
		print(fh.read())
		fh.close()
	elif sel == 2:
		fh = open(filen, "a")
		fh.write(input("Write a new note: ") + ":::" + time.strftime("%X %x") + "\n")
		fh.close()
	elif sel == 3:
		fh = open(filen, "w")
		fh.close()
	elif sel == 4:
		filen = input("Give the name of the new file: ")
		try:
			fh = open(filen, "r")
			fh.close()
		except IOError:
			fh = open(filen, "w")
			fh.close()
			print("No notebook with that name detected, created one.")

	elif sel == 5:
		break
	else:
		print("Incorrect selection")
		
print("Notebook shutting down, thank you.")