# Copyright (c) 2018 Cais Team. All Rights Reserved.

import sys
from termcolor import *
import os

"""
The CAIS Programming Language.
CAIS Original Compiler.
"""

lang = []
l = 0

def finish(file):
    with open(file, 'w') as f:
        f.truncate()
        f.close()
    quit()

def read(file):
    global l
    global finalf

#    finalf = file[:-4] + ".py"
#    finalf = os.path.abspath(finalf)
    finalf = "cache/file.py"
    finalf = os.path.abspath(finalf)
    finished = False

    while not finished:
        with open(file) as f:
            for line in f.readlines():
                l+=1
                if line[:11] == "#use <cais>":
                    lang.append("cais")
                elif "cais" not in lang:
                    cprint("CAIS: file {}: Line {}. \n ".format(finalf, l), "red")
                    cprint("CAIS: Unknown language or framework.", "red")
                    finish(finalf)
                elif line[:6] == "write " and "cais" in lang:
                    if line[-2] == "\"" or line[-1] == "\"":
                        add(finalf, "write", line[7:][:-2])
                    else:
                        cprint("CAIS: file {}: Line {}. \n ".format(finalf, l), "red")
                        cprint("    {}".format(line), "red")
                        cprint("Syntax Error: Write method was given an unknown argument.", "red")
                        finish(finalf)
                elif line[:7] == "cwrite " and "cais" in lang:
                    if line[-2] == "\"" or line[-1] == "\"":
                        add(finalf, "cwrite", line[8:][:-2], color="red")
                    else:
                        cprint("CAIS: file {}: Line {}. \n ".format(finalf, l), "red")
                        cprint("    {}".format(line), "red")
                        cprint("Syntax Error: Color Write method was given an unknown argument.", "red")
                        finish(finalf)
                elif line[:3] == "ask" and "cais" in lang:
                    return
                elif (line[:2] == "//") or (line[:2] == "/#") or (line[:2] == "\n"):
                    ignore = True
                else:
                    cprint("CAIS: file {}: Line {}. \n ".format(finalf, l), "red")
                    cprint("    {}".format(line), "red")
                    cprint("CAIS: Syntax Error.", "red")
                    finish(finalf)
                finished = True
    run(finalf)

def run(file):
    cmd = "python3 " + file
    os.system(cmd)
    cprint("CAIS: Program finished with exception O.", "blue")
    print("\033[1mCAIS: Object 'file' located at %s.\033[0m" %(sys.argv[1]))
    finish(file)

def add(file, statement, text=None, color=None):
    with open(file, "a") as f:
        f.write("from termcolor import * \n")
        if statement == "write":
            if text is not None:
                f.write("print(\"" + text + "\") \n")
        if statement == "cwrite":
            if text is not None:
                f.write("cprint(\"" + text + "\", \"" + color + "\")")

try:
    read(sys.argv[1])
except FileNotFoundError:
    cprint("Cais: No such file or directory: \"{}\"".format(sys.argv[1]), "red")
