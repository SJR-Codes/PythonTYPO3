# -*- coding: cp1252 -*-

class MyError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

raise MyError("There are four lights.")


raise SyntaxError


# -*- coding: cp1252 -*-
num = input("Give a number: ")

try:
	int(num)
	print("The input was suitable!")
except ValueError:
	print("The input was malformed.")

# -*- coding: cp1252 -*-
filen = input("Give the file name: ")

try:
	fh = open(filen, "r")
	data = int(fh.read())
	print("The result was", 1000/data)
	fh.close()
except ValueError:
	print("The file contents were unsuitable.")
except IOError:
	print("There seems to be no file with that name.")

class Switch:
	"""Switcher-class, returns a Boolean."""
	__mode = False

	def get_mode(self):
		return self.__mode

	def switch_mode(self):
		if self.__mode == False:
			self.__mode = True
		else:
			self.__mode = False

class [Name]:
    [attribute_1] = [default value]
    ...
    [attribute_N] = [defaul value]
    def [method name](self,[parameters]):
        [function code]

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)

# -*- coding: cp1252 -*-
class Cart:
	"""This class manages the shopping cart. """
	
	shoppingcart = []
	def addstuff(self):
		esine = input("What will be added?: ")
		self.shoppingcart.append(esine)

	def checkout(self):
		print("Following objects were added:")
		for i in range(0,len(self.shoppingcart)):
			print(self.shoppingcart[i], end = " ")

def main():
	customer = Cart()
	while True:
		selection = input("Add more or go to checkout?: ")
		if selection == "checkout":
			customer.checkout()
			break
		else:
			customer.addstuff()
		
if __name__ == "__main__":
	main()


# -*- coding: cp1252 -*-
class Cart:
    """This class manages the shopping cart. """
    
    shoppingcart = []
    def addstuff(self):
        esine = input("What will be added?: ")
        self.shoppingcart.append(esine)

    def checkout(self):
        print("Following objects were added:")
        for i in range(0,len(self.shoppingcart)):
            print(self.shoppingcart[i], end = " ")

class SmallerCart(Cart):
    """This is a small cart with limited space"""
    size = 2
    def checkout(self):
        print("Following was added: ")
        for i in range(0,self.size):
            print(self.shoppingcart[i])
        if len(self.shoppingcart) > self.size:
            print("Some items were left out.")

def main():
    customer = SmallerCart()
    while True:
        selection = input("Add more or go to checkout?: ")
        if selection == "checkout":
            customer.checkout()
            break
        else:
            customer.addstuff()
            
if __name__ == "__main__":
    main()


# -*- coding: cp1252 -*-

import pickle

listexample = ["Pineapple", "Atlas", ("Shaft", "Blade"), 1150]
filename = open("saveme.dat","wb")
print(listexample)
pickle.dump(listexample,filename)

filename.close()