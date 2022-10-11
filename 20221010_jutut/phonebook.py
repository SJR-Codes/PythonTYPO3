"""
* Taitotalo Python 10.10.2022
* phonebook.py
* description
* Created by Samu Reinikainen
"""

def add_number(phonebook: dict) -> None:
    '''Adds new entry to phonebook or updates existing number'''
    name = input("Nimi: ")
    number = input("Numero: ")
    phonebook.update({name: number})
    print("Puhelinumero lisätty.")

def find_number(phonebook: dict) -> str:
    '''Find and return phonenumber for given name'''
    name = input("Nimi: ")
    number = phonebook.get(name, False)
    if number:
        print("Numero:", number)
    else:
        print("Numeroa ei löydy!")

def main():
    phonebook = {}
    while True:
        act = int(input("Toiminto (1: hae, 2: lisää, 3: lopeta): "))
        if act == 3:
            break
        elif act == 2:
            add_number(phonebook)
        elif act == 1:
            find_number(phonebook)

    print("Puhelinluettelo: ", phonebook)

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()