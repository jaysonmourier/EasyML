from colorama import Fore

def fatal(code: int, msg: str):
    print(Fore.RED + '[FATAL] ' + msg)
    exit(code)