import sys
from termcolor import *
import os
import webbrowser
import time
import random

cai = "cessentials.cai"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def install(file, path, readme=None):
    path = path + ".cai"
    with open(path) as f:
        f.write("/# Standalone CAIS Essentials Setup File: \n")
        f.write("/# This code is crucial for CAIS Essentials Plugin to work. \n")
        f.write("/# \n")
        f.write("/# Copyright (c) 2018 Dev3 Team, CAIS Team, CAIS Essentials Development Team. All Rights Reserved.")
        f.write(file)
        if readme != None:
            f.write(readme)
        return path

cprint("Initializing CAIS Plugin Installer v1.0.")
cprint("Welcome to CAIS Plugin Installer v1.0.", "blue")
cprint("Now you will install \"CAIS Essentials\" Plugin, made by \"CAIS Essentials Team\".", "green")
cprint("This install also includes \"CAIS Essentials\" license provided by \"CAIS Plugin Licenser\".", "green")
awnser = input(bcolors.WARNING + "Are you sure you want to install? [Y/N]: " + bcolors.ENDC)
if awnser.upper() == "N":
    cprint("You cancelled plugin installation. Now exiting...", "red")
    print(awnser.upper())
else: # The user wrote something else than N (normally expected "Y")
    cprint("Starting Installation...")
    cprint("Awaiting Refresh (DON'T DO ANYTHING!)")
    time.sleep(3)
    cprint("Installing CEssentials.cai...", "blue")
    with open("test.cai") as f:
        f.write(cai)
