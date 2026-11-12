#Import Libraries
import os
import getpass
import time
import json

import tinytag
from tinytag import TinyTag

# File paths
user_data = 'dat/login_info.json'
music_folder = 'dat/music'

# Global Variables
users_information = json.load(open(user_data))

# Script Classes
class Color:
    WARNING = '\033[31m'
    NORMAL = '\033[97m'
# Define script functions
def home_page():
    clear_screen()
    print(f'''{Color.NORMAL}██╗  ██╗ ██████╗ ███╗   ███╗███████╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝
███████║██║   ██║██╔████╔██║█████╗  
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                    ''')
    print('=========================================================================')
    print('1. Library\n2. Playlists\n3. Settings')
    print('=========================================================================')
    user_input = input()
    if user_input == '1':
        clear_screen()
        print('Downloaded Songs: ')
        if not os.listdir(music_folder):
            print(f'{Color.WARNING}\nNo Music Found!')
        else:
            for i in os.listdir(music_folder):
                info = TinyTag.get(f'{music_folder}/{i}')
                print(info.title)


def clear_screen() -> None:
    # I use linux so it checks if ur on Windows or linux and clears the previous text from the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

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
            if users_information[username_i][0] == password_i:
                print('\nSuccess!')
                time.sleep(1)
                home_page()
            else:
                print(f'\n{Color.WARNING}Password does not match!')
                time.sleep(3)
                login_page()
        except KeyError:
            print('\nUser not found!')
            time.sleep(3)
            login_page()

    if u_input == '2':
        clear_screen()
        print('=========================================================================\nCREATE AN ACCOUNT')
        username_i: str = input('\nUSERNAME: ')
        password_i: str = getpass.getpass('PASSWORD: ')
        print('=========================================================================\nGETTING TO KNOW YOU')
        dob: str = input('\nDate of Birth: ')
        fav_artist: str = input('\nFavorite Artist: ')
        fav_genre: str = input('\nFavorite Genre: ')
        try:
            print('Setting up your account now...')
            # Writes a list into the dictionary key so multiple values can be stored in one key
            users_information[username_i] = [password_i, dob, fav_artist, fav_genre]
            # json.dumps converts a python dictionary into json format so it can be written
            convert = json.dumps(users_information)
            with open (user_data, 'w') as file:
                file.write(convert)
                file.close()
        except KeyError:
            print('Error during account creation')
            time.sleep(3)
            login_page()
login_page()