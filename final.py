#--------------------------------including classes and system files----------------------------------------------------------------------------

from dropbox import client, rest, session
from Tkinter import Tk
from tkFileDialog import askopenfilename

import webbrowser
import Tkinter, tkFileDialog
import shutil
import gnupg

#-------------------------------upload file class----------------------------------------------------------------------------------------------

def uploadfile():
	root = Tkinter.Tk()
	#select the file of your choice
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
	print "Before Encryption"
	print file 
	out="encrypted.txt.gpg"
	encrypted_ascii_data = gpg.encrypt_file(file,'girish' ,output=out,passphrase="random")
	#Use the comment and passphrase given during key generation for encryption.
	f = open("encrypted.txt.gpg", 'rb')
	response = client.put_file("encrypted.txt.gpg", f)
	print 'uploaded: ', response


#------------------------------download file class---------------------------------------------------------------------------------------------

def downloadfile():
	root = Tkinter.Tk()
	#selects the file to be decrypted from the dropbox app in the loacal system, change the path accordingly!
	file = tkFileDialog.askopenfile(parent=root,initialdir="/home/girish/Dropbox/Apps/Giri_python",mode='rb',title='Choose a file')
	print "Before Decryption"
	print file
	decrypted_data = gpg.decrypt_file(file, output='decrypted.txt')
	print "downloaded"

#------------------------------defyning gpg----------------------------------------------------------------------------------------------------

gpg = gnupg.GPG()
public_keys = gpg.list_keys()

"""
App key and Secret from the Dropbox developer website
AUthenticating the app code snipet was derived from the site
https://www.dropbox.com/developers/core/start/python
"""

APP_KEY = '1s6pm4h0f04xivk'
APP_SECRET = '393rypodegjkdl5'

#-----ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app---------------------------------------------------------------

ACCESS_TYPE = 'app_folder'

#-----------------obtain the request token-----------------------------------------------------------------------------------------------------

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
 
request_token = sess.obtain_request_token()

"""
Make the user sign in and authorize this token
Token and session code snipet was derived from the site
https://www.dropbox.com/developers/core/start/python
"""

url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
webbrowser.open_new(url)
raw_input()


# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
 
client = client.DropboxClient(sess)
print "linked account:", client.account_info()

# Uploading a file

print "File uploading"
uploadfile()

#Download a file

print "File downloading"
downloadfile()


#--------------------------------------------------------------END-----------------------------------------------------------------------------


