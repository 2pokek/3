import pyAesCrypt

password = input('Enter password: ')

# pyAesCrypt.encryptFile('random.txt','random.txt.aes',password)

pyAesCrypt.decryptFile('random.txt.aes','derandom.txt',password)