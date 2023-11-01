import zipfile
import os
from colorama import Fore, Style
import time
import subprocess

os.system('cls' if os.name == 'nt' else 'clear')
def execute_file(file_path):
    subprocess.call(['python', file_path])

execute_file('Pass-Wiz/bnr.py')
execute_file('Pass-Wiz/start.py')
time.sleep(2)

def extract_zip(zip_file, password):
    global start_time
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(pwd=bytes(password, 'utf-8'))
        os.system('clear' if os.name == 'posix' else 'cls')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{Fore.GREEN}Password Cracked successfully!{Style.RESET_ALL}")
        print(f"Password found after {attempts} attempts.")
        print(f"Time taken to find the password: {elapsed_time:.2f} seconds")
        print(f"{Fore.CYAN}Correct password: {password}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Owner: SUKH-H4CKER{Style.RESET_ALL}")
        input("Press Enter to restart the tool.")
        return True
    except Exception as e:
        print(f"{Fore.RED}Password incorrect: {password}{Style.RESET_ALL}")
        return False

def main():
    zip_file_path = input("\033[96mEnter the path to the ZIP file: ")
    password_list_path = input("\033[96mEnter the path to the password list file: ")

    with open(password_list_path, 'r') as password_file:
        passwords = password_file.read().splitlines()

    global attempts
    attempts = 0
    global start_time
    start_time = time.time()

    for password in passwords:
        attempts += 1
        if extract_zip(zip_file_path, password):
            break
        else:
            print(f"{Fore.RED}Sorry Password Not Cracked!")

if __name__ == "__main__":
    main()
