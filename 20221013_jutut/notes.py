#notes for 13.10.2022

names = []

    #for _ in range(3):
    name = input("Give name: ")
    foo = input("Foo bar: ")
    #    names.append(name)

    #for name in sorted(names):
    #    print(f"Hello, {name}")

    filen = "names.csv"
    #file = open(filen, "a") #w = write, a = append
    #file.write(name + "\n")
    #file.close()

    #pythonic way
    with open(filen, "a") as file:
        file.write(name + "," + foo + "\n")

    readfile()
"""
def readfile():
    filen = "names.txt"
    with open(filen, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(f"Hello, {line}", end="")
"""

def readfile():
    filen = "names.csv"
    """
    filen = "names.txt"
    with open(filen, "r") as file:
        for line in file:
            print("Hello, ", line.rstrip())
    """

    """
    names = []
    with open(filen, "r") as file:
        for line in file:
            names.append(line.rstrip())
    for name in sorted(names):
        print(f"Hello, {name.title()}")
    """
    """
    lines = []
    with open(filen, "r") as file:
        for line in file:
            lines.append(line.rstrip())
    for line in sorted(lines):
        #row = line.rstrip().split(",")
        name, foo = line.rstrip().split(",")
        #print(f"Hello, {row[0].title()} from {row[1]}")
        print(f"Hello, {name.title()} from {foo}")
    """

    students = [] # empty list

    with open(filen, "r") as file:
        for line in file:
            name, foo = line.rstrip().split(",")
            #student = {} #empty dict
            #student["name"] = name
            #student["foo"] = foo
            student = {"name": name, "foo": foo}
            students.append(student)

    #for student in sorted(students, key=get_name):
    #for student in sorted(students, key=get_foo):
    #lambda functions, anonymous funcs
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name'].title()} from {student['foo']}")

def get_name(student):
    return student["name"].title()

def get_foo(student):
    return student["foo"]
