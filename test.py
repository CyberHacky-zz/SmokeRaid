import os
import sys
import csv
import pandas as pd 



print ("[+] SmokeRaid | Run All Analysis : \n")

#details = os.system('autorunsc.exe -h -c') 

details = os.system('PECMD.exe -f C:\Windows\Prefetch\MIMIKATZ.EXE-BE95302C.pf')

with open('filename.txt', 'a') as f:
    print(details, file=f)

    #os.system('autorunsc.exe -h -ct')
    #os.system('PECMD.exe -f C:\Windows\Prefetch\MIMIKATZ.EXE-BE95302C.pf')
    #os.system('loki.exe')
    
    


   
