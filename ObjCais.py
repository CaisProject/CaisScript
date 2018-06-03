# Copyright (c) 2018 CAIS Team.
#
# CAIS Object Interpreter (not object-orineted paradigm)
# ObjCais: CAIS interpreer for cobj and objects.
# For CAIS interpreter see: ICAIS.
# For CAIS compiler see: CCAIS.
# This interpreter works for .cobj files.
# For a .lang interpreter see: LCAIS

import sys
from termcolor import *
import webbrowser
import CAISinfo as i
objects = {
    "1" : "console",
    "2" : "webbrowser",
    "3" : "interpreter",
    "4" : "compiler",
    "5" : "Perin"
}

using_console = False
current_obj = []
_version_ = 1.0
args = []
i = 0
show_message = True
functions = []

def read(file):
    with open(file) as f:
        if show_message:
            cprint("ObjCais Interpreter v{}".format(float(_version_)), "blue")
        if f.readline(11) == "#use <cais>":
            for line in f.readlines():
                if line[:8] == "@console" or line[:12] == "@use.console":
                    current_obj_sin = "console" # console also equals 1.
                    using_console = True
                    # for current in current_obj:
                        # if current != "console":
                            # current_obj.remove(current)
                    current_obj.append(current_obj_sin)
                elif line[:11] == "@webbrowser" or line[:15] == "@use.webbrowser":
                    current_obj_sin = "webbrowser" # webbrowser also equals 2.
                    #for current in current_obj:
                    #    if current != "console":
                    #        current_obj.remove(current)
                    current_obj.append(current_obj_sin)
                # if line[9:] ==

                if line[:4] == "dfc ":
                    lenght = len(line)
                    name1 = line[4:]
                    i = 0
                    m = 0
                    for name in name1:
                        i += 1
                        if name == "(":
                            break
                    func_name = line[4:][:i-1]
                    functions.append(func_name)
                    for z in line[4:][i:]:
                        m += 1
                        if z == ")":
                            break

                    args.append(line[4:][i:][:m-1])

                if line[:16] == "    console.out(" or line[:8] == "\tconsole.out(":
                    print(line[17:][:-3])
                elif line[:12] == "console.out(":
                    print(line[13:][:-3])

                if line[:17] == "    console.show(":
                    if line[17:][:-2] == "debugger=False":
                        print("")
                if line[:2] == "/#":
                    return("")
                if line[:6] == "exit;" or line[:7] == "exit;\n" or line[:8] == "exit;\n":
                    break
        else:
            error("CallOut exception", "CAIS needs to be called.")
            error_show("1")

def error(type, error_log, exit=False, inline=True):
    if inline:
        cprint(type + ":", "red")
        cprint(error_log, "red")
    else:
        cprint(type + ": " + error_log, "red")
    if exit:
        quit()

def error_show(line_num, code=None, expected=None):
    cprint("Line: {}".format(line_num), "red")
    if code != None:
        cprint(code)

try:
    read(sys.argv[1])
except FileNotFoundError:
    cprint("CAIS: There's no shuch file or directory known as {}.".format(sys.argv[1]), "red")
quit()
