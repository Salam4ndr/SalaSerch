# this is the introduction to the tool

from rich import print

print('''
[green]


 _____       _       _____                     _     
/  ___|     | |     /  ___|                   | |    
\ `--.  __ _| | __ _\ `--.  ___  __ _ _ __ ___| |__  
 `--. \/ _` | |/ _` |`--. \/ _ \/ _` | '__/ __| '_ \ 
/\__/ / (_| | | (_| /\__/ /  __/ (_| | | | (__| | | |
\____/ \__,_|_|\__,_\____/ \___|\__,_|_|  \___|_| |_|
                                                                                                
                      
|---------------------------------------------------|
| tool made by Salam4ndr to search for hidden pages |                              
|---------------------------------------------------|
''')

# import the library
import requests
import sys
from take_data import take_data
from enumeration import enumeration


# here start main.... 


# take the url and wordlist
url,wordlist = take_data()


# print the attack settings
print(f''' [green]
    --------------settings-------------------


     url => {url}\n
     wordlist => {wordlist}\n
     Version => 1.0\n
     Type => GET 

    ------------Octopus-ssh------------------
''')

# start enumeration
enumeration(url,wordlist)


# end 

print("\n\n[bold green][+] thanks for using my tool :))\n")
