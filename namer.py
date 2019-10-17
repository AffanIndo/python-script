
"""
namer.py
Select the option and let the program rename the files according to the option selected.
The idea of this program is to compile all of the common repetitive task of renaming files.
For example, if the option for remove underscore is 1 and the option to remove parentheses is 2,
you can use 2 command at once by typing "12" or 21.
"""

import os
import glob

option = []

def parentheses():
    """
    remove all parentheses in file name
    example:
    file (1).txt => file 1.txt
    """
    files = glob.glob("*(*).*")
    for file in files:
        new_name = file.replace("(", "")
        new_name2 = new_name.replace(")", "")
        print(new_name2)
        os.rename(file, new_name2)

def underscore():
    """
    remove all underscore in file name
    example:
    file_1.txt => file 1.txt
    """
    files = glob.glob("*_*")
    for file in files:
        new_name = file.replace("_", " ")
        os.rename(file, new_name)

def hd():
    """
    remove all _HD in file name
    example:
    video_HD.mp4 => video.mp4
    """
    files = glob.glob("*_HD*")
    for file in files:
        new_name = file.replace("_HD", "")
        os.rename(file, new_name)

def replace():
    """
    replace something in file name
    example:
    >>> Search: Asd
    >>> Replace: Def
    fileAsd.txt => fileDef.txt

    Delete something in file name
    example:
    >>> Search: Asd
    >>> Replace:
    fileAsd.txt => file.txt
    """
    search = input("Search: ")
    replace = input("Replace: ")
    files = glob.glob("*" + search + "*")
    for file in files:
        new_name = file.replace(search, replace)
        os.rename(file, new_name)

def random():
    """
    randomize file name
    example:
    >>> How many digit?: 5
    file.txt => 78349.txt
    """
    import random
    while True:
        try:
            retry = 0
            digit = int(input("How many digit?: "))

            files = glob.glob("*.*")
            for file in files:
                # number creator
                new_name_list = []
                name_list = [] # name for all files
                temp_name = []
                ext = file.split(".")[1]
                for i in range(digit):
                    randomNumber = str(random.randint(1, 9))
                    temp_name.append(randomNumber)
                name_list.append("".join(temp_name)) # joining all the number
                for name in name_list:
                    new_name_list.append(name + "." + ext) # adding file format into new_name_list
                for name in new_name_list:
                    os.rename(file, name)
            break
        except FileExistsError:
            print("FileExistsError: Input the digit again or increase the digit.")

def prefix():
    """
    add prefix to file name
    example:
    >>> Prefix: Asd
    file.txt => Asdfile.txt
    """
    prefix = input("Prefix: ")
    files = glob.glob("*.*")
    for file in files:
        os.rename(file, prefix+file)
        print(file)

def suffix():
    """
    add suffix to file name
    example:
    >>> Suffix: Asd
    file.txt => fileAsd.txt
    """
    suffix = input("Suffix: ")
    files = glob.glob("*.*")
    for file in files:
        os.rename(file, file+suffix)
        print(file)

# the problem with prefix() is that it will add prefix to ALL files. with number() it will add prefix to matching filename
def number(): # add zero prefix => if desired digit is n, search file with n-1 digit then add 1 zero prefix so desired digit achieved
    """
    Add zero(s) to file name
    example:
    >>> Desired digit?: 3
    01.jpeg => 001.jpeg
    """
    digit = int(input("Desired digit?: "))
    files = glob.glob("[0-9]" * (digit-1) + (".*")) # search file with n-1 digit
    for file in files:
        os.rename(file, "0"+file) # add 1 zero prefix

def text():
    """
    Rename files according to a txt file.
    example:
    >>> File: file.txt
    Separate search and replace with |
    file1.txt|data.txt
    file2.txt|log.txt

    file1.txt => data.txt
    file2.txt => log.txt
    """
    text_file = input("File: ")
    with open(text_file, "r") as f:
        for line in f:
            search = line.split("|")[0].replace("\n", "")
            replace = line.split("|")[1].replace("\n", "")
            os.rename(search, replace)
            Change

# main program
def main():
    # program user interface
    print("""
    1. Parentheses remover
    2. Underscore remover
    3. Tubemate"s _HD remover
    4. Search and replace
    5. File name randomizer
    6. Prefix
    7. Suffix
    8. Number Namer
    9. Renaming From A Text File
    """)

    # option parser
    select = input("Option: ")
    for item in select:
        option.append(item) # pushing the option into the list
    for options in option: # executing each option in the list
        if options == "1": # calling the function name
            parentheses()
            print("Command " + options + " success!")
        elif options == "2":
            underscore()
            print("Command " + options + " success!")
        elif options == "3":
            hd()
            print("Command " + options + " success!")
        elif options == "4":
            replace()
            print("Command " + options + " success!")
        elif options == "5":
            random()
            print("Command " + options + " success!")
        elif options == "6":
            prefix()
            print("Command " + options + " success!")
        elif options == "7":
            suffix()
            print("Command " + options + " success!")
        elif options == "8":
            number()
            print("Command " + options + " success!")
        elif options == "9":
            text()
            print("Command " + options + " success!")
        else:
            print("Command " + options + " not found!")

if __name__ == "__main__":
    main()