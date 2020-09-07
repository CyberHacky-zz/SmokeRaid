#!/usr/bin/env python3

import os
import sys
import os
import csv

#Title print

logo = ('''
     
   _____                 _        _____       _     _ 
  / ____|               | |      |  __ \     (_)   | |
 | (___  _ __ ___   ___ | | _____| |__) |__ _ _  __| |
  \___ \| '_ ` _ \ / _ \| |/ / _ \  _  // _` | |/ _` |
  ____) | | | | | | (_) |   <  __/ | \ \ (_| | | (_| |
 |_____/|_| |_| |_|\___/|_|\_\___|_|  \_\__,_|_|\__,_|
                                                      
                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!]         Created By : www.smokescreen.io\n\n''')


# Print Logo on startup
print(logo)


def mainmenu():
    print ("""
   {1}--Autorunsc
   {2}--PeCMD
   {3}--LoKI
   {4}--Mimikatz
   {0}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        autorunsc()
    elif choice == "2":
        pecmd()
    elif choice == "3":
        loki()
    elif choice == "4":
        mimikatz()
    elif choice == "0":
        print("Thanks for Using Smokeraid")
        os.system('cls'), sys.exit()
    elif choice == "":
        print(logo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        mainmenu()
    else:
        print(logo)
        mainmenu()


# Run Autorunsc from here

def autorunsc():
    

    print ("""
   {1}--All Entries
   {2}--Boot Executes
   {3}--Show File Hashes
   {4}--Print tab-delimited values
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        allentries()
    elif choice == "2":
        bootexc()
    elif choice == "3":
        filehash()
    elif choice == "4":
        tabdelval()
    elif choice == "0":
        os.system('cls')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using SmokeRaid")
        os.system('cls'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        autorunsc()
    else:
        print(logo)
        mainmenu()

#run autorunsc commands here

def allentries():
    os.system('cls')
    print(logo)
    print ("[+] Autorunsc | All Entries Listout Here : \n")

    os.system('autorunsc.exe *')
    autorunsc()

def bootexc():
    os.system('cls')
    print(logo)
    print ("[+] Autorunsc | Boot Executes Listout Here : \n")

    os.system('autorunsc.exe b')
    autorunsc()

def filehash():
    os.system('cls')
    print(logo)
    print ("[+] Autorunsc | File Hashes Listout Here : \n")

    os.system('autorunsc.exe -h')
    autorunsc()

def tabdelval():
    os.system('cls')
    print(logo)
    print ("[+] Autorunsc | All Entries Listout Here : \n")

    os.system('autorunsc.exe -ct')
    autorunsc()



#PECMD Commands run here

def pecmd():

    print ("""
   {1}--Help - Know all Commands
   {2}--All Perefetch List
   {3}--Find Mimikatz 
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        pecommandknow()
    elif choice == "2":
        allprefetch()
    elif choice == "3":
        findmimi()
    elif choice == "0":
        os.system('cls')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using SmokeRaid")
        os.system('cls'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        pecmd()
    else:
        print(logo)
        mainmenu()

def pecommandknow():

    os.system('cls')
    print(logo)
    print ("[+] PeCMD | All Prefetch Listout Here : \n")

    os.system('PECMD.exe')
    pecmd()


def allprefetch():

    os.system('cls')
    print(logo)
    print ("[+] PeCMD | Find Mimikatz Here : \n")

    os.system('PECmd.exe -d "C:\Windows\Prefetch')
    pecmd()


# Run Loki Here





# Run Mimikatz Here



def mimikatz():

    print ("""
   {1}--Mimikatz Commands
   {2}--Version Information
   {3}--Privilage Debug
   {4}--Hostname Information
   {5}--Logon Password Details
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        mimihelp()
    elif choice == "2":
        versioninfo()
    elif choice == "3":
        privide()
    elif choice == "4":
        hostinfo()
    elif choice == "5":
        logonpass()
    elif choice == "0":
        os.system('cls')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using SmokeRaid")
        os.system('cls'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        mimikatz()
    else:
        print(logo)
        mainmenu()



# Run mimikatz commands

def mimihelp():

    os.system('cls')
    print(logo)
    print ("[+] Mimikatz | Find Commnads : \n")

    os.system('mimikatz.exe help')

    mimikatz()

def versioninfo():

    os.system('cls')
    print(logo)
    print ("[+] Mimikatz | Find Version Information : \n")

    os.system('mimikatz.exe version')
    
    mimikatz()

def privide():

    os.system('cls')
    print(logo)
    print ("[+] Mimikatz | Privilege Debug Mode : \n")

    os.system('mimikatz.exe privilege::debug')
   
    mimikatz()

def hostinfo():

    os.system('cls')
    print(logo)
    print ("[+] Mimikatz | Find Hostname : \n")

    os.system('mimikatz.exe hostname')
    
    mimikatz()

def logonpass():

    os.system('cls')
    print(logo)
    print ("[+] Mimikatz | Find Logon Password : \n")

    os.system('mimikatz.exe sekurlsa::logonpasswords')
    
    mimikatz()

# Call main menu to run program
mainmenu()