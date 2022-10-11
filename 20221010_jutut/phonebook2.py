"""
* Taitotalo Python 10.10.2022
* phonebook.py
* description
* Created by Samu Reinikainen
"""

def add_number(phonebook: dict) -> None:
    '''Adds new entry to phonebook or updates existing record'''
    name = input("Nimi: ")
    number = [input("Numero: ")]
    if name in phonebook:
        number.append(*phonebook.get(name))
    phonebook.update({name: number})
    print("Puhelinumero lisätty.")

def find_number(phonebook: dict) -> None:
    '''Find and return phonenumber for given name'''
    name = input("Nimi: ")
    number = phonebook.get(name, False)
    if number:
        print("Numero(t):")
        for numb in number:
            print(numb)
    else:
        print("Numeroa ei löydy!")

def del_number(phonebook: dict) -> None:
    '''Deletes record for given name'''
    name = input("Nimi: ")
    number = phonebook.get(name, False)
    if number:
        phonebook.pop(name)
        print(f"{name} poistettu luettelosta.")
    else:
        print("Nimeä ei löydy luettelosta!")

def get_action(phonebook: dict) -> None:
    acts = {
        1:{'act':'find_number()', 'show': 'Hae'},
        2:{'act':'add_number()', 'show': 'Lisää'},
        3:{'act':'del_number()', 'show': 'Poista'},
        4:{'act':'print()', 'show': 'Tulosta'},
        5:{'act':'break', 'show': 'Lopeta'}
    }

    while True:
        print("Toiminto", end="")
        for a in acts:
            print(" ", a, ": ", acts[a].get('show'), sep="", end="")
        try:
            action = int(input(": "))
            real_action = acts[action].get('act').replace('()', '(phonebook)')
            #print(real_action)
            if real_action != 'break':
                eval(real_action)
            else: 
                break
        except ValueError:
            print("Koitappa 1,2,3,4 tai 5...")

def main():
    phonebook = {}
    get_action(phonebook)

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()