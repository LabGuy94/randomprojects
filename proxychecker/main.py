timeouttime = 3
threadsamount = 100


#------ DONT EDIT BELLOW -----#
import requests
import threading
import random
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
                print("working")
                o = open("validproxies.txt","a+")
                o.write(f"{randomproxy['https'].replace('http://', '')}\n")
            except:
                checkedproxies.append(randomproxy)
                print("failed") 
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
