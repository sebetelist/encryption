# GPG encryption based on AES-256
The program encrypts data using the AES-256 algorithm and places the result in a file. Data is read from a file and output on the screen. 
## Requirements
- python version 3.8 or higher [download](https://www.python.org/downloads/);
- installed git [download](https://git-scm.com/downloads);
- installed gnupg library. To install it input in terminal:
**pip install gnupg**
## Start
You must be in the same directory as the file.
### Linux
**python3 gpg.py**
### Windows
Check version **python --version** or **python3 --version**

Depending on the version of python:
**python3 gpg.py** or **python gpg.py**
## Usage
There are two modes - **encryption** and **decryption**. Data is encrypted using a passphrase. 
Next, the file name is written, without specifying the extension. For example: *secret*. 
The files are automatically created with the *.key* extension. 
To decrypt, you also need to specify the file name without the *.key* extension and then enter the passphrase. 
