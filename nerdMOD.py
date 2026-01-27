# == nerdMOD - 1.0_alpha ==
# a python module made by randomnerd41

import os
import sys
import time

def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
        
def wait(wt):
    time.sleep(wt)
    
def FOSS():
    print("this program is FOSS")
    time.sleep(2)
    clear()
    
def update_debian():
    yes = input("do you 100% want to update your system? (y/n) ")
    if yes == "y":
        os.system('sudo apt update -y && sudo apt upgrade -y')
        clear()
    else:
        print("will not update")
        time.sleep(3)
        clear()
        
def update_arch():
    yee = input("do you 100% want to update your system? (y/n) ")
    if yes = "y":
        os.system("sudo pacman -Syu")
    else:
        print("will not update")
        time.sleep(3)
        clear()
        
def update_arch_yay():
    ehh = input("do you 100% want to update your systen with yay? (y/n) ")
    if ehh = "y":
        os.system('yay -Syu')
    else:
        print("will not update")
        time.sleep(3)
        clear()

