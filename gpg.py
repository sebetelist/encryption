#import os
from gnupg import GPG
from pathlib import Path
from pwinput import pwinput
import json
from generator import get_unique_file
from sys import exit

with open('config.json', 'r', encoding='utf-8') as f: conf = json.load(f)

gpg = GPG()
gpg.encoding = 'utf-8'
styles, ui = conf['styles'], conf['ui']


# Encryption
def encrypt():
    try:
        while True:
            data = input(ui['input_data'])
            if not data:
                print(f"{styles['error']}{ui['error_empty']}{styles['reset']}")
                continue
            break

        base = 'file'
        ext = conf['settings']['extension']
        file_path = get_unique_file(base, ext)
        password = pwinput(prompt=ui['input_password'], mask='*')
        symmetric = conf['settings']['cipher']
        
        encryption = gpg.encrypt(data, 
                                recipients=None, 
                                symmetric=symmetric, 
                                passphrase=password,
                                output=str(file_path))

        if (encryption.ok):
            print(f"{styles['info']}{ui['success_encryption']} -> {file_path}{styles['reset']}")
        else:
            print(f"{styles['error']}{ui['error_input']}{styles['reset']}")
    except Exception:
        print(f"{styles['error']}{ui['error_corruption']}{styles['reset']}")


# Decryption
def decrypt():
    folder = "files"
    while True:
        file_name_input = input(ui['input_file'])
        if not file_name_input:
            print(f"{styles['error']}{ui['error_empty']}{styles['reset']}")
            continue
        break

    file_name = file_name_input + conf['settings']['extension']
    file_path = Path(folder) / file_name

    password = pwinput(prompt=ui['input_password'], mask='*')
    try:
        with open(file_path, 'rb') as f:
            decryption = gpg.decrypt_file(f, passphrase=password)
            if decryption.ok:
                print(f"{styles['info']}{ui['success_decryption']}{styles['reset']}\n{decryption}")
            else:
                print(f"{styles['error']}{ui['error_input']}{styles['reset']}")

    except FileNotFoundError:
        print(f"{styles['error']}{ui['error_file']}{styles['reset']}")
    except PermissionError:
        print(f"{styles['error']}{ui['error_permission']}{styles['reset']}")
    except OSError:
        print(f"{styles['error']}{ui['error_corruption']}{styles['reset']}")
    except Exception:
        print(f"{styles['error']}{ui['error_corruption']}{styles['reset']}")


def quit_program():
    print(f"{styles['error']}{ui['exit_message']}{styles['reset']}")
    exit()

actions = {'1': encrypt, '2': decrypt, '3': quit_program}

while True:
    try:
        choice = input(ui['menu'])
        action = actions.get(choice)
        if choice == '3':
            quit_program()
        elif action:
            action()
        else:
            print(ui.get('error_choice', '?'))
    except KeyboardInterrupt:
        quit_program()
