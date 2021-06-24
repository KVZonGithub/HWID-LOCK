import pyperclip
import subprocess
import requests
from time import sleep
import sys
from colorama import Fore
import os

try:
            hwid = subprocess.check_output('wmic csproduct get UUID').decode().split('\n')[1].strip()
            rekes = requests.get('TON PASTEBIN')

            try:
                if hwid in rekes.text:
                    chars = ['|', '/', '-', '\\', '|', '/', '-', '\\' ] 
                    for char in chars:
                        sys.stdout.write('\r'+'[+] '+'En attente d\'HWID... '+char)
                        sleep(0.9)
                        sys.stdout.flush()
                    os.system("cls")
                    print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Tu es connecté à la base données.")
                    sleep(2.8)
                else:
                    print(f"HWID: {hwid}")
                    pyperclip.copy(hwid)
                    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Tu n'es pas dans la base de données. Contacte Merryzz et donne lui ton HWID. (HWID copié dans le presse-papier).") 
                    sleep(5)
                    sys.exit()
            except:
                print("Erreur")
except:
      print("Erreur de connexion. Vérifie ton Internet")
        
os.system("cls")

# Do not skid or copy this code.
# Developped by KVZ ! 
# > KVZ.#0001