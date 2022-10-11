"""
* Taitotalo Python 22.09.2022
* word_len.py
* Ask for word and print its length if longer than 1.
* Created by Samu Reinikainen
"""

def main():
    """
    function desc
    :raise Error: error cond
    :return: returns what
    :rtype: return type
    """
    
    try:
        wrd = input("Say word: ")
        word_len = len(wrd)
        if word_len > 1:
            print(f"Your word '{wrd}' is {word_len} chars long.")
            print("Kiitos!")
        else:
            print("Not a word!")
    except:
        exit("Error: error msg")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()