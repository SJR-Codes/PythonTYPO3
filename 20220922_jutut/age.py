"""
* Taitotalo Python 22.09.2022
* age.py
* Ask users age and calculate when they are 100 years old.
* Created by Samu Reinikainen
"""

import datetime

def main():
    """
    function desc
    :raise Error: error cond
    :return: n/a
    :rtype: return n/a
    """
    
    today = datetime.date.today()
    year_now = int(today.strftime("%Y"))


    try:
        user_name = input("What's your name: ")
        age = int(input("How old are you in years: "))
        birth_year = year_now-age+100

        print(f"Hi {user_name}, you were born in {birth_year}")
    except ValueError:
        exit("Error: age not valid number!")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()