timeouttime = 3
threadsamount = 100

#----- DONT EDIT BELLOW -----#

import requests
import threading
import random
import time
from colorama import Fore

number_of_proxies = len(open('proxies.txt').readlines(  ))
with open("validproxies.txt", 'r+') as f:
    f.truncate(0)


clearConsole = lambda: print('\n' * 150)
clearConsole()
print(Fore.BLUE + """

 ██▓    ▄▄▄       ▄▄▄▄     ██████      █████▒▄▄▄        ██████ ▄▄▄█████▓    █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀     ██████ ▓█████  ███▄    █ ▓█████▄ ▓█████  ██▀███  
▓██▒   ▒████▄    ▓█████▄ ▒██    ▒    ▓██   ▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒   ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██░   ▒██  ▀█▄  ▒██▒ ▄██░ ▓██▄      ▒████ ░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░   ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██░   ░██▄▄▄▄██ ▒██░█▀    ▒   ██▒   ░▓█▒  ░░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄      ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░██████▒▓█   ▓██▒░▓█  ▀█▓▒██████▒▒   ░▒█░    ▓█   ▓██▒▒██████▒▒  ▒██▒ ░    ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
░ ▒░▓  ░▒▒   ▓▒█░░▒▓███▀▒▒ ▒▓▒ ▒ ░    ▒ ░    ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░      ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░ ▒  ░ ▒   ▒▒ ░▒░▒   ░ ░ ░▒  ░ ░    ░       ▒   ▒▒ ░░ ░▒  ░ ░    ░         ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░ ░    ░   ▒    ░    ░ ░  ░  ░      ░ ░     ░   ▒   ░  ░  ░    ░           ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░    ░  ░  ░     ░      ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
    ░  ░     ░  ░ ░            ░                  ░  ░      ░                  ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░            ░     ░  ░         ░    ░       ░  ░   ░     
                       ░                                                                         ░                                                                 ░                      
""")
print(Fore.BLACK + "Created By LabGuy94#6666")
print(Fore.MAGENTA + "Config")
print(Fore.MAGENTA + "Threads:")
print(Fore.MAGENTA + str(threadsamount))
print(Fore.MAGENTA + "Proxies Loaded")
print(Fore.MAGENTA + str(number_of_proxies))
print(Fore.MAGENTA + "Timeout Time:")
print(Fore.MAGENTA + str(timeouttime))
print(Fore.MAGENTA + "starting in 5 secconds")
clearConsole = lambda: print('\n' * 8)
clearConsole()
time.sleep(5)
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]
checkedproxies = []
def checkproxies():
    for proxy in proxies:
        global checkedproxies
        if(not proxy in checkedproxies):
            try:
                randomproxy = random.choice(proxies)
                checkedproxies.append(randomproxy)
                r = requests.get('https://httpbin.org/ip', proxies=randomproxy, timeout=timeouttime)
                print(Fore.GREEN + "✅ Working")
                o = open("validproxies.txt","a+")
                o.write(f"{randomproxy['https'].replace('http://', '')}\n")
            except:
                checkedproxies.append(randomproxy)
                print(Fore.RED + "❌ Failed")
threads = []

for i in range(threadsamount):
    t = threading.Thread(target=checkproxies)
    t.daemon = True
    threads.append(t)

for i in range(threadsamount):
    threads[i].start()

for i in range(threadsamount):
    threads[i].join()
print("Done")
