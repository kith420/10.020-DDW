from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'idklol' #set later for random 16 byte password

cipher = AES.new(key,AES.MODE_CBC)

plaintext = b'this is my super secret message to encrypt'

ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))

with open('cipher_file', 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)