#!/usr/bin/env python3

import os
import sys
import csv
import pandas as pd 

#Title print

logo = ('''
     
   _____                 _        _____       _     _ 
  / ____|               | |      |  __ \     (_)   | |
 | (___  _ __ ___   ___ | | _____| |__) |__ _ _  __| |
  \___ \| '_ ` _ \ / _ \| |/ / _ \  _  // _` | |/ _` |
  ____) | | | | | | (_) |   <  __/ | \ \ (_| | | (_| |
 |_____/|_| |_| |_|\___/|_|\_\___|_|  \_\__,_|_|\__,_|
                                                      
                                                                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!]            Created By : CyberHacky\n\n''')


# Print Logo on startup
print(logo)


def mainmenu():
    print ("""
   {1}--Autorunsc
   {2}--PeCMD
   {3}--LoKI
   {4}--Mimikatz
   {5}--Run All Analysis
   {6}--VirusTotal Analysis
   {7}--Run WMI Script
   {8}--Remove WMI Script
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
    elif choice == "5":
        allanalysis()
    elif choice == "6":
        virustotal()
    elif choice == "7":
        wmiscript() 
    elif choice == "8":
        wmiremovescript() 
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
    print ("[+] PeCMD | Find Commands : \n")

    os.system('PECMD.exe -h')
    pecmd()



def allprefetch():

    os.system('cls')
    print(logo)
    print ("[+] PeCMD | Find All Prefetch Here : \n")

    os.system('PECmd.exe -d "C:\Windows\Prefetch')
    pecmd()

def findmimi():

    os.system('cls')
    print(logo)
    print ("[+] PeCMD | Find Mimikatz Here : \n")

    os.system('PECMD.exe C:\Windows\Prefetch\MIMIKATZ.EXE-BE95302C.pf')
    pecmd()

# Run Loki Here

def loki():

    print ("""
   {1}--Help - Know all Commands
   {2}--Scan Machine
   {3}--Read Logs 
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        lokicommandknow()
    elif choice == "2":
        scanmachine()
    elif choice == "3":
        readlog()
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


## Run Loki commmand here

def lokicommandknow():

    os.system('cls')
    print(logo)
    print ("[+] LoKI | Find Commands Here : \n")

    os.system('loki.exe -h')
    loki()


def scanmachine():

    os.system('cls')
    print(logo)
    print ("[+] LoKI | Scan Machine : \n")

    os.system('loki.exe')
    loki()


def  readlog():

    os.system('cls')
    print(logo)
    print ("[+] LoKI | Read Logs : \n")

    os.system('loki.exe -l ')
    loki()




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




#Run All analysis

def allanalysis():

    os.system('cls')
    print(logo)
    print ("[+] SmokeRaid | Run All Analysis : \n")

    autocsv = os.system('autorunsc.exe -ct > autorun_output.csv') 

    pecmdcsv = os.system('PECMD.exe -f C:\Windows\Prefetch\MIMIKATZ.EXE-BE95302C.pf > pecmd_file.csv')

    lokicsv =  os.system('loki.exe > lokioutput.csv')

    print(' [!] Bingo -  Analysis Saved in CSV File [!] ')

    
    mainmenu()


    print("Hello stackoverflow!", file=open("output.txt", "a"))

# Run WMI Script
def wmiscript():

    os.system('cls')
    print(logo)
    print ("[+] SmokeRaid | Run WMI Script : \n")
    os.system('wmi.ps1')

    mainmenu()


# Remove WMI Script
def wmiremovescript():

    os.system('cls')
    print(logo)
    print ("[+] SmokeRaid | Remove WMI Script : \n")
    os.system('wmiremove.ps1')

    mainmenu()



# Run VirusTotal Analysis

def virustotal():

    mainmenu()


# Call main menu to run program
mainmenu()