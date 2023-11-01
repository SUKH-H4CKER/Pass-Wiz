# Importing the necessary modules
import sys
import webbrowser
import subprocess
import os
import time

def execute_file(file_path):
    subprocess.call(['python', file_path])

execute_file('Pass-Craft/src/bnr.py')
execute_file('Pass-Craft/src/bnr.py')
execute_file('Pass-Craft/src/start.py')
time.sleep(2)

def main():
    print('''\n\n\033[96m**Tool Description:**
This tool is a zip file password cracking utility that uses brute-force techniques to search for zip file passwords. It comes with an advanced password list generator that can create password lists according to the user's specific requirements.

**Warning:**
The use of this tool is strictly for educational purposes. Do not use this tool for any illegal activities or to crack the passwords of zip files without proper authorization.

**License:**
This tool is subject to a license, and the owner's name must be "SUKH-H4CKER." It is mandatory to credit the owner "SUKH-H4CKER" when using this tool.

**Modification Warning:**
If you are considering making any modifications to this tool or using it in an unauthorized manner, please be aware that the owner "SUKH-H4CKER" may take strict and legal actions against you. Use this tool thoughtfully and within the boundaries of the law.

**Owner's Name:**
Make sure to include the name of the owner "SUKH-H4CKER" everywhere you use this tool and provide proper credit.'''
)
    user_input = input("\033[92m\nEnter 'tg' (Telegram) or 'ig' (Instagram) to visit a specific social media, or simply press Enter to stop the tool: ")

    if user_input == "tg":
        # Redirect to your Telegram channel
        tg_url = "https://t.me/SUKH_H4CKER_GROUP"  # Replace with your Telegram channel URL
        webbrowser.open(tg_url)

    elif user_input == "ig:
        # Redirect to your Instagram profile
        insta_url = "https://instagram.com/__king_of_hackers__?igshid=MzNlNGNkZWQ4Mg=="  # Replace with your Instagram profile URL
        webbrowser.open(insta_url)

    elif not user_input:
        # Tool stops if the user enters an empty input
        print("Tool has been stopped.")

    else:
        # Tool stops for any other input
        print("Tool has been stopped.")

if __name__ == "__main__":
    main()

