import os
try:
    from colorama import *
except:
    print("You do not have the Colorama Module, Please wait we are installing it...")
    os.system("pip install colorama")
    os.system("pip3 install colorama")
    print("Finished, restart this program")
import hashlib
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

passlist = open("passwords.txt", "r").read().splitlines()
hits = open("hits.txt", "w")
count = 0

print(Fore.CYAN + ascii)
print("\n")

time.sleep(3)

for line in passlist:
    count = count + 1

    txt = line
    txtencoded = txt.encode('utf-8')

    hash = hashlib.md5(txtencoded)
    hexa = hash.hexdigest()

    print(Fore.CYAN + "[" + Fore.GREEN + "+" + Fore.CYAN + "] " + Fore.WHITE + "Successfully hashed » " + hexa + " [" + str(count) + "]")
    hits.write(hexa + " [" + line + "]\n")

hits.close()