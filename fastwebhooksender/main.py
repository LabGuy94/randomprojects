#----- EDIT THIS -----#
threadsamount = 5
message = "@everyone"
webhooks = ["https://discord.com/api/webhooks/865901064564899840/8dA-xzpK0977SpuO3fZZIeQYKiRePQegzxCsTSmI8dyhFJwvZAj9oT0OYQSmtADwtAaz", "https://discord.com/api/webhooks/865901158559645766/pQDiYTgBqCx2WBeBqbvuLb6IoR8gWIpls70IENIuEIa41L98VltJMv_fxaBFh5q1E6Q7", "https://discord.com/api/webhooks/865901183569494056/FsjpZNnnIyKRoWwsHMbz0CCmEBkvZmjp5_n1-KsDRuIuNVRw2LF1E7gI_vl7Tf_J807x", "https://discord.com/api/webhooks/865901210385252352/plJQQ7ssXA3ShM0u6C_BxauMYrfDFuP1hSthwHjuRYVgrSePbh5iEx7fGSD4dDPfJRz1", "https://discord.com/api/webhooks/865901237940256799/To8xJ1KiCjifMANm1IXA-Q6afqFoxpRQ-t5G9H-jK4uXtYuZjFzBxhoETWIoeTGT4qKJ", "https://discord.com/api/webhooks/865901266693783552/E5nWaL_SEv3W9z4mBe395pvgOf8EWcUhOYxccy1zr8zp-Gpjnq-vM2ituosh1JvjF2Rw", "https://discord.com/api/webhooks/865901293288423474/dMeElydaC-ECX9ru_y-ceQLNlPEQCCTZRV2YcqXYKz-bWCa9COUrHlT6Wwws0HOQkV5K", "https://discord.com/api/webhooks/865901319390363680/KYhogopV4ntXRP9KABGRoj2T0fHWtgzGPQxv3Eq4yZepwM4ChSEamzZA2kw7BwU5pCw5", "https://discord.com/api/webhooks/865901346619129896/cCk5rL2fIrbq34gVEkSSj0ex5adXdWSHVfQQBLEX5mc7t4pW2SsKM5VeeTesHfZO_VTZ", "https://discord.com/api/webhooks/865901372292333598/c5kNXfu9C0FSOZMsptQZE33J2r2jHIrujVkmQBe8DxKMT59q10FMJ81QmCEoosJAaLpo"]
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
