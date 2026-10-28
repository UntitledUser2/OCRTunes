#Import Libraries
import platform
import subprocess
import getpass
import time

# Global Variables
users_information = {'Hello':'123'}

# Script Classes
class Color:
    WARNING = '\033[31m'
    NORMAL = '\033[97m'
# Define script functions
def clear_screen() -> None:
    # I use linux so it checks if ur on windows or linux and clears the previous text from the terminal
    if platform.system() == 'Linux':
        subprocess.run('clear')
    else:
        subprocess.run('cls')

def login_page() -> None:
    clear_screen()
    # ASCII Art
    print(f'''{Color.NORMAL} ██████╗  ██████╗██████╗    ████████╗██╗   ██╗███╗   ██╗███████╗███████╗
██╔═══██╗██╔════╝██╔══██╗   ╚══██╔══╝██║   ██║████╗  ██║██╔════╝██╔════╝
██║   ██║██║     ██████╔╝█████╗██║   ██║   ██║██╔██╗ ██║█████╗  ███████╗
██║   ██║██║     ██╔══██╗╚════╝██║   ██║   ██║██║╚██╗██║██╔══╝  ╚════██║
╚██████╔╝╚██████╗██║  ██║      ██║   ╚██████╔╝██║ ╚████║███████╗███████║
 ╚═════╝  ╚═════╝╚═╝  ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                        ''')
    print('=========================================================================')
    print('LOGIN or SIGNUP\n1. Log In\n2. Sign Up')
    u_input: str = input('\n')

    if u_input == '1':
        clear_screen()
        print('=========================================================================')
        # Get pass library makes it so when the user enters their password it is hidden
        username_i: str = input('\nUSERNAME: ')
        password_i: str = getpass.getpass('PASSWORD: ')
        try:
            if users_information[username_i] == password_i:
                print('Success!')
            else:
                print(f'\n{Color.WARNING}Password does not match!')
                time.sleep(3)
                login_page()
        except KeyError:
            print('\nUser not found!')
            time.sleep(3)
            login_page()


login_page()