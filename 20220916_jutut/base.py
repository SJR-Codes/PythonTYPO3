"""
* Taitotalo Python 16.09.2022
* Base & notes
* by Samu Reinikainen
"""

"""
* Taitotalo Python 16.09.2022
*  base.py
*  description
*  Created by Samu Reinikainen
"""

def main():
    print(f"Hello, {function_tmpl()}!")
    print(hello())
    
def hello() -> str:
    """
    Return hello world string
    :raise Error: if something goes wrong
    :return: string
    :rtype: string
    """
    
    try:
        return "Hello world!"
    except:
        exit("Error: unknown error")

# base function template
def function_tmpl() -> str:
    """
    Does what functions do
    :raise Error: If something goes wrong
    :return: string or something
    :rtype: string
    """

    try:
        ret_str = "World"

        return ret_str
    #this should be more specific
    except:
        exit("Error: something went wrong")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()