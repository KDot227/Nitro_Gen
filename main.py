import random
import string
import threading
import requests # on everything if someone comes to my server saying that "Requests is slow use aiohttp or urllib3" ill ban u on site im not playing wit u"
import os
from pystyle import *
import time

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")

print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))

print(Colors.green + "Welcome to prolly the fastest discord nitro code generator ever made. (in python)")
print("")

num = int(input("How many codes do you want to generate? -> "))
webhook = input("Enter your webhook url (leave blank if you don't want to use a webhook) -> ")
total_threads = int(input("How many threads do you want to use? (NOTE DONT DO OVER 50 OR PC MIGHT HAVE A TOUGH TIME) -> "))

start_time = time.time()

def main():
    number = threading.get_native_id()
    with open(f"NITRO_CODES_{number}.txt", "w", encoding="utf-8") as f:
        for i in range(num):
            code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
            f.write(f"https://discord.gift/{code}\n")
    with open(f"NITRO_CODES_{number}.txt", "r", encoding="utf-8") as f:
        codes = f.read().splitlines()
        for code in codes:
            r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if r.status_code == 200:
                print(Colors.blue + f"[+] Valid Nitro Code: {code}" + Colors.reset)
                try:
                    requests.post(webhook, json={"content": f"Valid Nitro Code: {code}"})
                except:
                    input("Press Enter to exit...")
                    exit()
            else:
                print(Colors.green + f"[-] Invalid Nitro Code: {code}")
        print(Colors.blue + "No nitro codes found..." + Colors.reset)
    os.remove(f"NITRO_CODES_{number}.txt")


threads = []

if __name__ == "__main__":
    for i in range(total_threads):
        t = threading.Thread(target=main)
        threads.append(t)
    for x in threads:
        x.start()
    for x in threads:
        x.join()
    print("")
    print(Colors.purple + "Finished All codes!!!")
    total_codes = num * total_threads
    print(f"Generated {total_codes} codes in {time.time() - start_time} seconds! (pretty fast ik) (smd)")
    input("Press Enter to exit...")
    exit()