# -*- coding: cp1252 -*-
class Player:
	"""Player-class: stores data on team colors and points."""
	def __init__(self):
		self.color = input("What color do I get?: ")
		self.points = 0

	def printout(self):
		print(f"The {self.color} contender has {self.points} points!")
	
	def tellscore(self):
		print(f"I am {self.color}, we have {self.points} points!")

	def goal(self):
		self.points += 1

def main():
	pl1 = Player()
	pl2 = Player()
	pl1.goal()
	pl1.goal()
	pl2.goal()
	pl1.tellscore()
	pl2.tellscore()
		
if __name__ == "__main__":
	main()