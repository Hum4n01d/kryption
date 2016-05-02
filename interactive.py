from encryption import encode
from encryption import decode

while True:
    choice = input('Encode or decode? ').lower()

    if choice == 'encode':
        message = input('Message to encode: ')
        passphrase = input('Passphrase: ')
        
        encrypted = encode(message, passphrase)
        print('Encoded message: ' + encrypted)
    
    elif choice == 'decode':
        message = input('Message to decode: ')
        passphrase = input('Passphrase: ')
        decrypted = decode(message, passphrase)
        print('Decoded message: ' + decrypted)