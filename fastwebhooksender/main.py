#----- EDIT THIS -----#
threadsamount = 5
message = "@everyone"
webhooks = [""]
useproxies = True
timeouttime = 3


#------ DONT EDIT BELLOW ------#

import requests
import threading
import time
from colorama import Fore
import random
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]
data = {
    "content": message
}
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
print(Fore.BLACK + "Created by LabGuy94#6666")
print(Fore.MAGENTA + "Config")
print(Fore.MAGENTA + "Threads:")
print(Fore.MAGENTA + str(threadsamount))
print(Fore.MAGENTA + "Message")
print(Fore.MAGENTA + message)
print(Fore.MAGENTA + "Webhook")
print(Fore.MAGENTA + str(webhooks))
print(Fore.MAGENTA + "Using Proxies")
print(Fore.MAGENTA + str(useproxies))
print(Fore.MAGENTA + "Timeout Time")
print(Fore.MAGENTA + str(timeouttime))
print(Fore.MAGENTA + "starting in 5 secconds")
clearConsole = lambda: print('\n' * 8)
clearConsole()
time.sleep(5)
def do_request():
    while True:
        if useproxies == False:
            try:
                r = requests.post(random.choice(webhooks), json=data, timeout=timeouttime)
                if r.status_code == 429:
                    print(Fore.RED + "❌ Too many requests")
                if r.status_code == 204:
                    print(Fore.GREEN + "✅ Sucess")
            except:
                print(Fore.RED + "❌ Failed")
        if useproxies == True:
            try:
                r = requests.post(random.choice(webhooks), json=data, proxies=random.choice(proxies), timeout=timeouttime)
                if r.status_code == 429:
                    print(Fore.RED + "❌ Too many requests")
                if r.status_code == 204:
                    print(Fore.GREEN + "✅ Sucess")
            except:
                print(Fore.RED + "❌ Bad Proxy")
threads = []

for i in range(threadsamount):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(threadsamount):
    threads[i].start()

for i in range(threadsamount):
    threads[i].join()
