import os
import time

# Menu Options
while True:
    # Terminal ko clear karo (Windows aur Linux dono ke liye)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Banner file execute karo
    os.system('python Pass-Wiz/bnr.py')

    # Starting file execute karo
    os.system('python Pass-Wiz/start.py')

    # Note print karo cyan color mai
    print("\033[96m\nNote: Aapko zip file ka password crack karne ke liye ek password list ")
    print("\nOptions:")
    print("1. Password-List Generator")
    print("2. Password-Crack")
    print("3. About")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        # Password-List Generator
        os.system('python Pass-Craft/Pass-Craft.py')
    elif choice == '2':
        # Password-Crack
        os.system('python Pass-Wiz/Pass-Wiz.py')
    elif choice == '3':
        # About
        os.system('python Pass-Wiz/about.py')
    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        # Banner file execute karo
        os.system('python Pass-Wiz/bnr.py')

        # Starting file execute karo
        os.system('python Pass-Wiz/start.py')
        print('\033[96m\nExiting...')
        time.sleep(2)
        # Exit
        exit()
    else:
        print("Invalid choice. Please select a valid option.")
