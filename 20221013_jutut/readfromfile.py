"""
* Taitotalo Python 13.10.2022
* readfromfile.py
* description
* Created by Samu Reinikainen
"""

def main():
    '''Read names from nameslist and count'em'''
    filen = "nameslist.txt"
    names = {}
    with open(filen, "r") as file:
        for line in file:
            name = line.rstrip()
            if name in names:
                names[name] += 1
            else:
                names[name] = 1

    print(names)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()