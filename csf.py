# Copyright (c) 2018 CAIS Team. All Rights Reserved.
#
# This file is the interpreter for all .csf files.
# For the frameworks CSF supports see: /csf/frameworks.yml
#
import sys
from termcolor import *

using_cais = False
gui = None

def error(type, error_log, exit=False, newline=True):
    if newline:
        cprint(type + ":", "red")
        cprint(error_log, "red")
    else:
        cprint(type + ": " + error_log, "red")
    if exit:
        quit()

def read(file):
    global using_cais
    with open(file) as f:
        for line in f.readlines():
            if line[:10] == "#use <csf>":
                using_cais = True
            if not using_cais:
                error("CallOutError", "CSF needs to be called.", exit=True, newline=False)
            if line[:12] == "!b .cui -uim" and using_cais:
                gui = True


read(sys.argv[1])
quit()
