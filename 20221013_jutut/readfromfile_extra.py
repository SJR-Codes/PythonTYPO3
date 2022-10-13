"""
* Taitotalo Python 13.10.2022
* readfromfile_extra.py
* description
* Created by Samu Reinikainen
"""
import re

def main():
    '''Read names from nameslist and count'em'''
    filen = "Training_01.txt"
    cats = {}
    with open(filen, "r") as file:
        for line in file:
            cat = re.search("^\/.\/(.+?)\/sun_", line).group(1)
            #print(cat)
            if cat in cats:
                cats[cat] += 1
            else:
                cats[cat] = 1

    print(cats)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()