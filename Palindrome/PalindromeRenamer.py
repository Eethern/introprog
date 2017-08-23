__author__ = 'chrarvi'
import string
import Tkinter
import tkFileDialog
import os

def checker(wordToCheck):
    reversedWord = str(wordToCheck)[::-1].lower()
    if reversedWord == wordToCheck.lower():
        return True
    else:
        return False

def filter(wordToFilter):
    for i in wordToFilter:
        if i not in string.letters:
            wordToFilter = wordToFilter.replace(i,'')

    return wordToFilter

def readFile(path):
    temp = ""
    try:
        file = open(path, "r")
        temp = file.read()
        file.Close()
    except Exception as e:
        print(e)

    return temp

def init(words):
    count = 0
    wordList = words.split("\x20")

    for i, x in enumerate(wordList):
        x = filter(x)
        if checker(x):
            wordList[i] = x
            count += 1
            print x
        else:
            wordList[i] = ""

    wordList.remove("")

    print "There are a total of " + str (count) + " palindromes"

def ui():
    mode = raw_input("\nChoose mode: (I)nteractive, (R)ead from file or (E)xit.\n: ").lower()
    os.system("clear")
    if mode == "i":

        input = raw_input("Input string to check. (E)xit to exit.\n: ").lower()

        if input == "E":
            exit()
        else:
            init(input)


    elif mode == "r":

        rootTk = Tkinter.Tk()
        fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.txt"), ("All files", "*")))
        rootTk.destroy()

        if len(fname) > 0:
            init(readFile(fname))

    elif mode == "e":
        exit()
    ui()

if __name__ == "__main__":
    ui()


