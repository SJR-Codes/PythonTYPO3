"""
* Taitotalo Python 04.10.2022
* arvosanat.py
* description
* Created by Samu Reinikainen
"""
import math

def getGrades():
    grades = []
    while True:
        inp = input("Koepisteet ja harjoitusten määrä: ")
        if inp == "":
            return grades
        else:
            grades.append(inp)

def countStats(grades):
    epoints = []
    tpoints = []
    for grade in grades:
        row = grade.split()
        tpoints.append(int(row[0]))
        epoints.append(math.floor(int(row[1]) / 10))

    stats = []
    for index, points in enumerate(tpoints):
        stats.append(points + epoints[index])
    
    """ print("Points: ")
    print(epoints)
    print(tpoints)
    print("Stats: ")
    print(stats) """

    return stats

def countGrades(stats):
    results = []
    for res in stats:
        if res <= 14:
            results.append(0)
        elif res <= 17:
            results.append(1)
        elif res <= 20:
            results.append(2)
        elif res <= 23:
            results.append(3)
        elif res <= 27:
            results.append(4)
        else:
            results.append(5)
    """ print("Res: ")
    print(results) """

    return results

def countWholePoints(stats):
    wholePoints = 0
    for res in stats:
        wholePoints += res
    """ print("wholepoints: ")
    print(wholePoints) """

    return wholePoints

def printStats(grades):
    stats = countStats(grades)
    results = countGrades(stats)
    wholePoints = countWholePoints(stats)
    
    mean = wholePoints/len(results)
    accepted = 100 - (results.count(0)/len(stats)*100)

    print(f"Pisteiden keskiarvo: {mean:.1f}")
    print(f"Hyväksymisprosentti: {accepted:.1f}")

    for i in reversed(range(6)):
        amount = "*" * results.count(i)
        print(f"{i}: {amount}")

    
def main():
    #grades = getGrades()
    grades = ['15 87','10 55','11 40','4 17']
    #print(grades)
    print("Tilasto:")
    printStats(grades)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()