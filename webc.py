import requests
import colorama
import os
from colorama import Fore

green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
r = Fore.RESET

banner = """

   _____ _ _                     
  / ____(_) |                    
 | (___  _| |_ ___               
  \___ \| | __/ _ \              
  ____) | | ||  __/              
 |_____/|_|\__\___|              
  / ____| |                      
 | |    | | ___  _ __   ___ _ __ 
 | |    | |/ _ \| '_ \ / _ \ '__|
 | |____| | (_) | | | |  __/ |   
  \_____|_|\___/|_| |_|\___|_|   
                                 
                                 
""" 
os.system("clear")
print(green + banner+r)
print(red+'web page cloner by TWEETY | v 1.0'+r)

while True:
        get_url = input(yellow+"[+]Enter URL with http:// :  "+ r)
        if int(len(get_url)) < 1:
                print(red+"URL can not be empty" +r)
        else:
                break
get_file_name = input(yellow+"[+]Enter name of new html file  : "+r)

html = f"{get_file_name}.html"
try:
        req = requests.post(str(get_url))
        
except:
        os.system("clear")
        print(green + banner+r)
        print(yellow + "something went wrong " + r)
        print(red+"chek your url and make sure your internet connection is active" + r)
        
try:
        with open(html, "w+") as f:
                 f.write(str(req.text))
                 print(green+"[*]Done!"+r)
except:
        pass

