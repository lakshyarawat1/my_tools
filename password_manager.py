import os
import os.path
import argparse 
from cryptography.fernet import Fernet

def image() :
    print('''                                            _                                               
  _ __   __ _ ___ _____      _____  _ __ __| |  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |_) | (_| \__ \__ \\\ V  V / (_) | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ |   
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
 |_|                                                                        |___/           ''')

def intro() :
    print('Welcome to CODE-IO Password Manager')

def checkExistence():
    if os.path.exists('passwords.txt'):
        pass
    else :
        file = open('passwords.txt','w')
        file.close()
        
def checkKey() :
    if os.path.exists('filekey.key'):
        pass
    else : 
        keyfile = open('filekey.key','w')
        keyfile.close()
        
def verify() :
    identity = input("Verify your identity : ")
    if identity == 'hackerno8055' :
        print('Verified \n Welcome !! ')
        return 1
    else :
        print('Invalid Credentials \n Terminating')
        intro()
        return 0

def appendNew() :
    file = open('passwords.txt','a')

    print()
    print()
    
    userName = input("Enter the username : ")
    password = input("Enter the password : ")
    website = input("Enter the website : ")
    
    print()
    print()
    
    username = "Username : " + userName + '\n'
    passwrd = "Password : " + password + '\n'
    w3site = "Website : " + website + '\n'
    
    file.write('--------------------------------------------------------\n')
    file.write(username)
    file.write(passwrd)
    file.write(w3site)
    file.write('---------------------------------------------------------\n')
    file.write('\n')
    file.close()
    
def readPassword() :
    file = open('passwords.txt', 'r')
    content = file.read()
    file.close()
    print(content)
    
def encrypt() :
    checkKey()
    key = Fernet.generate_key()
    with open ('filekey.key','wb') as filekey:
        filekey.write(key)
    with open ('filekey.key', 'rb') as filekey :
        key = filekey.read()
        
    fernet = Fernet(key)
    
    with open('passwords.txt','rb') as file :
        original = file.read()
        
    encrypted = fernet.encrypt(original)
    
    with open('passwords.txt' ,'wb' ) as encrypted_file :
        encrypted_file.write(encrypted)

def decrypt() :
    with open ('filekey.key', 'rb') as filekey :
        key = filekey.read()
    fernet = Fernet(key)
    
    with open('passwords.txt', 'rb') as enc_file :
        encrypted = enc_file.read()
        
    decrypted = fernet.decrypt(encrypted)
    
    with open('passwords.txt','wb') as dec_file :
        dec_file.write(decrypted)

def clearFile() :
    checkExistence()
    checkKey()
    verified = verify()
    if verified == 0 :
        pass
    else : 
        os.remove('passwords.txt')
        os.remove('filekey.key')


parser = argparse.ArgumentParser()

parser.add_argument('-i','--intro', help='This is the default argument', default=1)
parser.add_argument('-r', '--write', help= " Lets you enter your passwords  ", action='store_true')
parser.add_argument('-s','--search', help='Lets you search a specific password ', action='store_true')
parser.add_argument('-e', '--encrypt', help='Encrypts the file', action='store_true')
parser.add_argument('-d','--decrypt', help='Decrypts the file', action='store_true')
parser.add_argument('-x','--delete',help='deletes the password file', action='store_true' )

args = parser.parse_args()

os.system('cls')
if args.intro :
    intro()
    image()

if args.write :
    
    checkExistence();
    if os.path.getsize('passwords.txt') == 0 :
        appendNew()
    else : 
        appendNew()
    
if args.search :
    checkExistence()
    if os.path.getsize('passwords.txt') == 0 :
        print("List is empty")
    else :
        readPassword()
if args.encrypt :
    checkExistence()
    encrypt()
    
if args.decrypt :
    checkExistence()
    verify()
    decrypt()
    
if args.delete :
    clearFile()