# -*- coding: cp1252 -*-
import random

def main():
    rsp = ["Foot","Nuke","Cockroach"]
    rounds = 0
    wins = 0
    ties = 0
    while True:
        usern = 0
        user = input("Foot, Nuke or Cockroach? (Quit ends): ").lower()
        if user == "foot": usern = 1
        elif user == "nuke": usern = 2
        elif user == "cockroach": usern = 3
        elif user == "quit": break
        else: print("Incorrect selection.")

        if usern > 0:
            rounds += 1
            print("You chose:", rsp[usern-1])
            comp = random.randint(1,3)
            print("Computer chose:", rsp[comp-1])
            if usern == comp:
                ties += 1
                if usern == 2: print("Both LOSE!")
                else: print("It is a tie!")
            elif comp == 1 and usern == 3: print("You LOSE!")
            elif comp == 2 and usern == 1: print("You LOSE!")
            elif comp == 3 and usern == 2: print("You LOSE!")
            else: 
                wins += 1
                print("You WIN!")
    

    print(f"You played {rounds} rounds, and won {wins} rounds, playing tie in {ties} rounds.")

if __name__ == "__main__":
    main()