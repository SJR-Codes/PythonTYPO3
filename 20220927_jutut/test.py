raja = 50 #int(input("Mihin asti: "))
kerroin = 5 #int(input("Mikä kerroin: "))
alku = 2

alku = 2**5

while alku < raja:
    print(alku)
    alku = alku**kerroin


# -*- coding: cp1252 -*-
a = input("Give the first number: ")
b = input("Give the second number: ")

# -*- coding: cp1252 -*-
print("Calculator")
a = int(input("Give the first number: "))
b = int(input("Give the second number: "))
print("The result is:", a+b)

# -*- coding: cp1252 -*-
print("Calculator")
a = int(input("Give the first number: "))
b = int(input("Give the second number: "))
print("(1) +\n(2) -\n(3) *\n(4) /")
c = int(input("Please select something (1-4): "))

if c == 1:
	print("The result is:", a+b)
elif c == 2:
	print("The result is:", a-b)
elif c == 3:
	print("The result is:", a*b)
elif c == 4:
	print("The result is:", a/b)
else:
	print("Selection was not correct.")


# -*- coding: cp1252 -*-
if input("Give name: ") == "John":
	if input("Give password: ") == "ABC123":
		print("Both inputs are correct!")
	else:
	   print("The password is incorrect.")
else:
	print("The given name is wrong.")