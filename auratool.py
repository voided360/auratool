import time
import requests
import platform
import subprocess
import os
from colorama import Fore, Style, init

init()

def clear():
    os.system("cls" if platform.system().lower() == "windows" else "clear")

def show_system_info():
    uname_info = platform.uname()
    print(f"\nSystem   : {uname_info.system}")
    print(f"Node     : {uname_info.node}")
    print(f"Release  : {uname_info.release}")
    print(f"Version  : {uname_info.version}")
    print(f"Machine  : {uname_info.machine}")
    print(f"Processor: {uname_info.processor}")

def ping_ip():
    ip = input("Enter IP or domain: ").strip()
    if not ip:
        print(Fore.RED + "No input given")
        return

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        subprocess.run(["ping", param, "4", ip])
    except:
        print(Fore.RED + "Ping failed")

def ip_lookup():
    ip = input("Enter IP address: ").strip()
    if not ip:
        ip = "me"

    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()

        print("\n--- IP Lookup Result ---")
        print("IP      :", data.get("query"))
        print("Country :", data.get("country"))
        print("City    :", data.get("city"))
        print("Region  :", data.get("regionName"))
        print("ISP     :", data.get("isp"))
    except:
        print(Fore.RED + "error")

while True:
    clear()
    print(Fore.BLUE + Style.BRIGHT + r"""
 ________  ___  ___  ________  ________  _________  ________  ________  ___          
|\   __  \|\  \|\  \|\   __  \|\   __  \|\___   ___\\   __  \|\   __  \|\  \         
\ \  \|\  \ \  \\\  \ \  \|\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \        
 \ \   __  \ \  \\\  \ \   _  _\ \   __  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \       
  \ \  \ \  \ \  \\\  \ \  \\  \\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \____  
   \ \__\ \__\ \_______\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\ \_______\ \_______\
    \|__|\|__|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|_______|\|_______|
""")

    print("made by kurre and voxy v1.0\n")

    print(Fore.BLUE + Style.BRIGHT +"1 show hwid info")
    print(Fore.BLUE + Style.BRIGHT +"coming soon")
    print(Fore.BLUE + Style.BRIGHT +"3 ping ip")
    print(Fore.BLUE + Style.BRIGHT +"4 ip lookup")
    print(Fore.BLUE + Style.BRIGHT +"5 exit")

    choice = input("\npick a choice 1-5: ")

    if choice == "1":
        show_system_info()
        input("\nPress ENTER to continue...")
        clear()

    elif choice == "3":
        ping_ip()
        input("\nPress ENTER to continue...")
        clear()

    elif choice == "4":
        ip_lookup()
        input("\nPress ENTER to continue...")
        clear()

    elif choice == "5":
        print("thanks for using aura")
        break

    else:
        print("Invalid option.")
        time.sleep(1)
        clear()