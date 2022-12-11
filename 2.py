import pyAesCrypt

password = input('Enter password: ')

pyAesCrypt.encryptFile('random.txt','random.txt.aes',password)