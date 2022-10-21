from config import Config
from colorama import init, Fore
import time
import colorama

colorama.init(autoreset=True)

class logs:

    def debug(message):
        print(Fore.YELLOW + f"({int(time.time())}) " + Fore.GREEN + "[+] DEBUG » " + Fore.BLUE + message)