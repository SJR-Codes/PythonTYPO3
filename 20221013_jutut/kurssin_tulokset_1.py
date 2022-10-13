"""
* Taitotalo Python 13.10.2022
* kurssin_tulokset.py
* description
* Created by Samu Reinikainen
"""

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

def main():
    opiskelijat = get_data("opiskelijat.csv")
    tehtavat = get_data("tehtavat.csv")
    #print(opiskelijat)
    #print(tehtavat)

    for id, vals in opiskelijat.items():
        print(*vals, get_count(tehtavat[id]))

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()