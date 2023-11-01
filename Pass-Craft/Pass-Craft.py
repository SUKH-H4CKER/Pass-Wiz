import os
import subprocess
import time
from colorama import init, Fore

init(autoreset=True)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def execute_file(file_path):
    subprocess.call(['python', file_path])

def main():
    while True:
        clear_terminal()
        execute_file('Pass-Craft/src/bnr.py')
        execute_file('Pass-Craft/src/start.py')
        time.sleep(2)
        print(f'{Fore.MAGENTA}\nSelect an Option: ')
        print('''
        1. Only Numbers
        2. Only Uppercase Letters
        3. Only Lowercase Letters
        4. Only Symbols
        5. Numbers + Lowercase Letters
        6. Numbers + Uppercase Letters
        7. Numbers + Symbols
        8. Uppercase + Lowercase Letters
        9. Uppercase + Symbols
        10. Lowercase + Symbols
        11. Uppercase + Lowercase + Numbers + Symbols
        12. About
        13. Exit
        ''')

        choice = input("Enter your choice: ")

        if choice == '1':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/number.py')
        elif choice == '2':
            clear_termina+l()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/uppercase.py')
        elif choice == '3':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/lowercase.py')
        elif choice == '4':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/symbols.py')
        elif choice == '5':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/num+lower.py')
        elif choice == '6':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/num+upper.py')
        elif choice == '7':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/num+symbol.py')
        elif choice == '8':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/upper+lower.py')
        elif choice == '9':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/upper+symbol.py')
        elif choice == '10':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/lower+symbol.py')
        elif choice == '11':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            execute_file('Pass-Craft/src/about.py')
        elif choice == '12':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            print(f'{Fore.CYAN}\nThanks for using Pass-Craft tool!')
            break
        elif choice == '13':
            clear_terminal()
            execute_file('Pass-Craft/src/bnr.py')
            execute_file('Pass-Craft/src/start.py')
            time.sleep(2)
            print(f'{Fore.CYAN}\nExiting Pass-Craft tool. Thanks for using it!')
            break
        else:
            print(f'{Fore.RED}Invalid choice. Please enter a valid option.')

if __name__ == '__main__':
    main()
