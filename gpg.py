from gnupg import GPG
from sys import exit

OKBLUE = '\033[96m'
FAIL = '\033[91m'
NC = '\033[0m'

gpg = GPG()
gpg.encoding = 'utf-8'


# crypt
def crypt():
    data = input('Data: ')

    encrypted = gpg.encrypt(str(data), recipients=None,
                            symmetric='AES256',
                            passphrase=input('Write a passphrase: '),
                            output=input('File name: ') + '.key'
                            )
    if (encrypted.ok):
        print(OKBLUE + 'Successfully encrypted!')
    else:
        print(FAIL + 'Wrong input')
    exit()


# decrypt
def decrypt():
    file = input('File name: ') + '.key'
    passphrase = input('Write a passphrase: ')
    with open(file, 'r') as f:
        text = f.read()
        decrypted = gpg.decrypt(str(text), passphrase=passphrase)
        if (decrypted.ok):
            print(decrypted)
        else:
            print(FAIL + 'Wrong passphrase')
        f.close()
        exit()


while True:
    mode = input('\nChoose mode:\n1.Crypt\n2.Decrypt\n3.Exit\n> ')
    if mode == '1':
        crypt()
    elif mode == '2':
        decrypt()
    elif mode == '3':
        break
    else:
        print(FAIL + 'Wrong input, retry again.' + NC)
