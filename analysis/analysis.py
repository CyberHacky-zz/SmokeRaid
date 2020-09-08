import pandas as pd
import hashlib
import os
import sys

def mainmenu():
    print ("""
   {1}--Autorunsc Hash
   {2}--PeCMD Hash
   {3}--LoKI Hash
   {0}--Exit
 """)
    choice = input("SmokeRaid~# ")
    if choice == "1":
        autorunscanalysis()
    elif choice == "2":
        peanalysis()
    elif choice == "3":
        lokianalysis()
    elif choice == "0":
        print("Thanks for Using Smokeraid")
        os.system('cls'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        mainmenu()
    else:
        mainmenu()

def autorunscanalysis():

    mylines = []                            
    with open ('autorun_output.txt', 'rt') as myfile: 
        for myline in myfile:                
            mylines.append(myline)           
        print(mylines[47])                          
        newautohash=(mylines[47])
  
# encoding newhash using encode() 
        result = hashlib.md5(newautohash.encode()) 
  
# printing the equivalent hexadecimal value. 
        print("The hexadecimal equivalent of hash is : ", end ="") 
        print(result.hexdigest()) 
        mainmenu()

def peanalysis():

    mylines = []                            
    with open ('pecmd_file.txt', 'rt') as myfile: 
        for myline in myfile:                
            mylines.append(myline)           
        print(mylines[47])                           
        newpehash=(mylines[47])
  
# encoding newhash using encode() 
        result = hashlib.md5(newpehash.encode()) 
  
# printing the equivalent hexadecimal value. 
        print("The hexadecimal equivalent of hash is : ", end ="") 
        print(result.hexdigest()) 
        mainmenu()

def lokianalysis():

    mylines = []                             
    with open ('lokioutput.txt', 'rt') as myfile: 
        for myline in myfile:                
            mylines.append(myline)           
        print(mylines[38])                           
        newpehash=(mylines[38])
  
# encoding newhash using encode() 
        result = hashlib.md5(newpehash.encode()) 
  
# printing the equivalent hexadecimal value. 
        print("The hexadecimal equivalent of hash is : ", end ="") 
        print(result.hexdigest()) 
        mainmenu()

# Call main menu to run program
mainmenu()

