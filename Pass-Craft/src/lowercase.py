import os
import itertools
import subprocess
import time

# Terminal ko clear karne ke liye Windows aur Linux ke liye alag commands
clear_command = "cls" if os.name == "nt" else "clear"

def execute_file(file_path):
    subprocess.call(['python', file_path])

execute_file('Pass-Craft/src/bnr.py')
execute_file('Pass-Craft/src/start.py')
time.sleep(2)

# Password length input
password_length = int(input("\033[96m\nEnter the password length: "))

# Default filename aur path
default_filename = "sukh_lower.txt"
default_path = ""

# Password generate aur save (only lowercase letters)
passwords = [''.join(x) for x in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=password_length)]

# User se filename input lena
user_filename = input("\033[96m\nEnter the filename for password storage (Press Enter for default): ")
if not user_filename:
    user_filename = default_filename

# User se path input lena
user_path = input("\033[96m\nEnter the path for password storage (Press Enter for default): ")
if not user_path:
    user_path = default_path

# Passwords save karne ki logic
with open(os.path.join(user_path, user_filename), "w") as file:
    for password in passwords:
        file.write(password + "\n")

# File details
file_name = f"File-Name: {user_filename}"
file_path = f"File-Path: {user_path}"
file_size = os.path.getsize(os.path.join(user_path, user_filename))
if file_size < 1024:
    file_size = f"File-Size: {file_size} bytes"
elif file_size < 1024 * 1024:
    file_size = f"File-Size: {file_size / 1024:.2f} KB"
else:
    file_size = f"File-Size: {file_size / (1024 * 1024):.2f} MB"

# Terminal ko clear karo
os.system(clear_command)

# Loading bar
total_combinations = 26 ** password_length
for i in range(1, total_combinations + 1):
    percent_complete = (i / total_combinations) * 100
    print(f"Loading: {percent_complete:.2f}%", end="\r")

execute_file('Pass-Craft/src/bnr.py')
execute_file('Pass-Craft/src/start.py')
time.sleep(2)

# Password file generated successfully message
print("\n\n\033[32m" + file_name)
print(file_path)
print(file_size)
print("\033[36mOwner: SUKH-H4CKER\033[0m")
print("\033[32mPassword File Generated Successfully!\033[0m")
input("\033[36mPress Enter To Continue!\n")
