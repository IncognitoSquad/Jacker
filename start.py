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

help = """\
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hashing Algorithms:
- md5
- sha1
- sha256
- sha512

Commands:
help - Display this menu
start (method) - Hash with a method
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

passlist = open("passwords.txt", "r").read().splitlines()

print(Fore.CYAN + ascii)
print("\n")

time.sleep(3)

print(Fore.CYAN + "Type help for help" + Fore.RESET)
def main():
    a = input("root@jacker~# ")
    if a.lower() == "help":
        print(Fore.CYAN + help + Fore.WHITE)
        main()
    if a.lower() == "start md5":
        md5()
    if a.lower() == "start sha1":
        sha1()
    if a.lower() == "start sha256":
        sha256()
    if a.lower() == "start sha512":
        sha512()
    else:
        print(Fore.RED + "Unknown Command" + Fore.WHITE)
        main()



def md5():
    count = 0
    a = input("Wordlist: ")
    if (os.path.isfile(a)):
        hits = open(a, "w")
        for line in passlist:
            count = count + 1

            txt = line
            txtencoded = txt.encode('utf-8')

            hash = hashlib.md5(txtencoded)
            hexa = hash.hexdigest()

            print(
                Fore.CYAN + "[" + Fore.GREEN + "+" + Fore.CYAN + "] " + Fore.WHITE + "Successfully hashed » " + hexa + " [" + str(
                    count) + "]")
            hits.write(hexa + " [" + line + "]\n")

        hits.close()
        main()
    else:
        print(Fore.RED + "File Does Not Exist!" + Fore.RESET)
        main()


def sha1():
    count = 0
    a = input("Wordlist: ")
    if (os.path.isfile(a)):
        hits = open(a, "w")
        for line in passlist:
            count = count + 1

            txt = line
            txtencoded = txt.encode('utf-8')

            hash = hashlib.sha1(txtencoded)
            hexa = hash.hexdigest()

            print(
                Fore.CYAN + "[" + Fore.GREEN + "+" + Fore.CYAN + "] " + Fore.WHITE + "Successfully hashed » " + hexa + " [" + str(
                    count) + "]")
            hits.write(hexa + " [" + line + "]\n")

        hits.close()
        main()
    else:
        print(Fore.RED + "File Does Not Exist!" + Fore.RESET)
        main()


def sha256():
    count = 0
    a = input("Wordlist: ")
    if (os.path.isfile(a)):
        hits = open(a, "w")
        for line in passlist:
            count = count + 1

            txt = line
            txtencoded = txt.encode('utf-8')

            hash = hashlib.sha256(txtencoded)
            hexa = hash.hexdigest()

            print(
                Fore.CYAN + "[" + Fore.GREEN + "+" + Fore.CYAN + "] " + Fore.WHITE + "Successfully hashed » " + hexa + " [" + str(
                    count) + "]")
            hits.write(hexa + " [" + line + "]\n")

        hits.close()
        main()
    else:
        print(Fore.RED + "File Does Not Exist!" + Fore.RESET)
        main()


def sha512():
    count = 0
    a = input("Wordlist: ")
    if (os.path.isfile(a)):
        hits = open(a, "w")
        for line in passlist:
            count = count + 1

            txt = line
            txtencoded = txt.encode('utf-8')

            hash = hashlib.sha512(txtencoded)
            hexa = hash.hexdigest()

            print(
                Fore.CYAN + "[" + Fore.GREEN + "+" + Fore.CYAN + "] " + Fore.WHITE + "Successfully hashed » " + hexa + " [" + str(
                    count) + "]")
            hits.write(hexa + " [" + line + "]\n")

        hits.close()
        main()
    else:
        print(Fore.RED + "File Does Not Exist!" + Fore.RESET)
        main()

main()

