import time
import sys
from termcolor import cprint
import os
import random

i = 0
vartype = ""
current_lang = []
statements = ["write", "if", "ask", "see if", "color", "class"]
def main(read):
    global current_lang
    global i
    global vartype
    with open(read) as f:
        for line in f.readlines():
            if line[:11] == "#use <cais>":
                current_lang.append("cais")
            if line[:6] == "write " and "cais" in current_lang :
                print(line[7:][:-3])
            elif line[:2] == "/#" or line[:2] == "//":
                ignore = True
            if line[:3] == "var":
                varname = line[5:]
                for char in varname:
                    i+=1
                    if char == ";":
                        i = 0
                        break
                    if char == "=":
                        break
                varvalue = line[i:][:-1]
                c = varvalue.count("\"")
                p = varvalue.count(".")
                if c == 2:
                    vartype = "string"
                elif c == 0 and varvalue.isdigit():
                    vartype = "integer"
                elif p == 1 and varvalue.isdigit():
                    vartype = "float"
                else:
                    vartype = "rtn 0"
                    if vartype == "rtn 0":
                        for char in varname:
                            t = 0
                            t+=1
                            if char == ";":
                                break
                        varname = line[:t]
                print("{} = {}. Is {}".format(varname, varvalue, vartype))
                #print(vartype)
try:
    main(sys.argv[1])
except FileNotFoundError:
    cprint("Cais: No such file or directory: \"{}\"".format(sys.argv[1]), "red")
