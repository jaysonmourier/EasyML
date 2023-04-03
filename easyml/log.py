from colorama import Fore

def info(msg):
    print(Fore.BLUE + "[INFO]", msg)

def fatal(code: int, msg: str, _exit:bool = True):
    print(Fore.RED + "[FATAL]", msg)
    if exit:
        exit(code)