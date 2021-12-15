from colorama import Fore

class Logger:
    def passed(self, log):
        print(F"{Fore.GREEN}PASS      :{Fore.RESET} {log}")
    def failed(self, log):
        print(F"{Fore.RED}FAIL      :{Fore.RESET} {log}")
    def in_progress(self, log):
        print(F"{Fore.BLUE}INPROGRESS:{Fore.RESET} {log}")
    def success(self, log):
        print(F"{Fore.GREEN}SUCCESS   :{Fore.RESET} {log}")
    def error(self, log):
        print(F"{Fore.LIGHTRED_EX}ERROR     :{Fore.RESET} {log}")
    def warning(self, log):
        print(F"{Fore.LIGHTYELLOW_EX}WARNING   :{Fore.RESET} {log}")
    def info(self, log):
        print(F"{Fore.LIGHTBLUE_EX}INFO      :{Fore.RESET} {log}")
