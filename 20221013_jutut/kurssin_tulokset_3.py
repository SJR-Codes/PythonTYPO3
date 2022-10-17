"""
* Taitotalo Python 13.10.2022
* kurssin_tulokset.py
* description
* Created by Samu Reinikainen
"""
import math

def get_data(filen = "") -> dict:
    if filen == "":
        filen = input("Anna tiedostonimi: ")
    ret = {}
    
    try:
        with open(filen, "r") as file:
            for line in file:
                osat = line.strip().split(";")
                if osat[0] != "opnro":
                    #print(type(osat[0]), type(osat[1:]))
                    ret[osat[0]] = osat[1:]
    except FileNotFoundError:
        print("Error: File not found")

    return ret

def get_count(data: list) -> int:
    '''Sum lists numbers together and return sum'''
    x = 0
    for i in data:
        x += int(i)

    return x

def count_points(i:int) -> int:
    '''Calc exercise points'''
    return math.floor((i/40)*100 / 10)

def count_grade(points:int):
    if points <= 14:
        grade = 0
    elif points <= 17:
        grade = 1
    elif points <= 20:
        grade = 2
    elif points <= 23:
        grade = 3
    elif points <= 27:
        grade = 4
    else:
        grade = 5

    return grade

def main():
    opiskelijat = get_data("opiskelijat.csv")
    tehtavat = get_data("tehtavat.csv")
    koepisteet = get_data("koepisteet.csv")
    #print(opiskelijat)
    #print(tehtavat)
    sarakkeet = {
        "nimi": 30,
        "teht_lkm": 10,
        "teht_pist": 10,
        "koe_pist": 10,
        "yht_pist": 10,
        "arvos": 10
    }
    for x, y in sarakkeet.items():
        print(f"{x:{y}}", sep="", end="")

    print()
    for id, vals in opiskelijat.items():        
        name = vals[0] + " " + vals[1]
        teht = get_count(tehtavat[id])
        points = count_points(teht)
        koep = get_count(koepisteet[id])
        yht = points + koep
        arvos = count_grade(yht)

        print(f"{name:30}{teht:<10}{points:<10}{koep:<10}{yht:<10}{arvos:<10}", sep="")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()