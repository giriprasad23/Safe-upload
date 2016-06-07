# Safe-upload

This is the readme file for the first assignment.The assignment is to upload an encrypted file and download the decrypted file to Dropbox.

Developed the program in linux environment-Ubuntu.
Programing language used is Python, software is python 2.7.5
Need to install gnupg and install necessarry packages. python-gnupg 0.3.6 for Python 2.7.5
Download the package from 'https://pypi.python.org/pypi/python-gnupg/' .
Download the Dropbox packages from the dropbox website, also install the dropbox app in the laptop.
User has to give his/her app_key and secret_key generated when creating app in Dropbox.
This program will upload and download files from that app.

The program uses Tkinter to select files to be uploaded or to be downloaded, need to install Tkinter. This can be done in ubuntu by running the below command in terminal, if not available. 
sudo apt-get install python python-tk idle python-pmw python-imaging


Need to generat keys for encryption and decryption.
Run the command gpg --gen-key in the terminal and give the inputs. 
Reffer 'https://help.ubuntu.com/community/GnuPrivacyGuardHowto' ,for details.




