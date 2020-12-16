import os
try:
    from colorama import *
except:
    print("You do not have the Colorama Module, Please wait we are installing it...")
    os.system("pip install colorama")
    os.system("pip3 install colorama")
    print("Finished, restart this program")
import time
init()

ascii = """\
 ▄▄▄██▀▀▀▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
   ▒██  ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
   ░██  ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓███▒   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▓▒▒░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░ ░    ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░   ░        ░  ░░ ░      ░  ░      ░  ░   ░     
                  ░                               """

print(Fore.CYAN + ascii)

f = open("hits.txt", "r").read().splitlines()
print("\n")

time.sleep(3)

def main():
    a = input("What Password Do you want to check for: ")
    for lines in f:
        if a in lines:
            print(Fore.GREEN + "Success » " + lines)
            main()
        else:
            print(Fore.RED + "Error » Could not find.")
            main()

main()