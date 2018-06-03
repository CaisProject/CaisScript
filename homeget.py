# Copyright (c) 2018 CAIS Team. All Rights Reserved.
#
# This is the Cais HomeGet's Code. For Homeget tests see /tests/test.hget.
#
import sys
from termcolor import *
import os.path
from os import path
from pathlib import Path

###############################################################################
#                               [hget files]
hgetsh = ""
yn = "no"
CAIS = os.path.join(os.path.expanduser('~'), 'CAIS')
homeget = CAIS + "/HomeGet"

hgeto = homeget + "/hget.cobj"
hgetl = homeget + "/hget.lang"

###############################################################################
#                             [text styles]
class text_style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

###############################################################################
#                                 [code]
def install(file_to_install):
    global yn
    if path.exists(hgeto):
        yn = "yes"
    cprint("homeget: checking for hget.cobj instance. -- " + yn, "blue")
    if path.exists(hgetl):
        yn = "yes"
    else:
        yn = "no"
    cprint("homeget: checking for hget.lang. -- " + yn, "blue")
    if yn == "no":
        print(text_style.BOLD + "1 error generated: " + text_style.END + "file[hget.lang]:")
        cprint("Could not detect hget.lang.", "red")
    

install("test")
