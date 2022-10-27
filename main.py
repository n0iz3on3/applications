from colorama import Fore, Style
from time import localtime, asctime, sleep
import application

tym = localtime()
opt = asctime(tym)

if __name__ == '__main__':
    print(f'{Fore.CYAN}In application dir is:\n{dir(application)}')
    sleep(1.0)
    print(f'{Fore.LIGHTMAGENTA_EX}Right now:\n{opt}')
    sleep(1.0)
    print(f'{Fore.LIGHTGREEN_EX}{application.salary.calculate_salary()}')
    sleep(1.0)
    print(f'{Fore.LIGHTYELLOW_EX}{application.people.get_employees()}')
    print(Style.RESET_ALL)