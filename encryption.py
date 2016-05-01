letters = '#c9f:nrb3pl/o<?G4^%F,V(}T~uQ$ghCÑ5&.eHj2LJd!¥€+ RkI[y>{S"]X@MK)OW\\wBa|vY681q7D£;=N-EiAzmP0UZ\'sx*t_•'

def encode(message, passphrase):
    encrypted = ''
    counter = 0
    
    for char in message:
        encrypted += letters[letters.index(char) + letters.index(passphrase[counter])]
        
        if counter == 3:
            counter = 0
        else:
            counter += 1

    return encrypted

def decode(message, passphrase):
    decrypted = ''

    counter = 0
    for char in message:
        decrypted += letters[letters.index(char) - letters.index(passphrase[counter])]
        
        if counter == 3:
            counter = 0
        else:
            counter += 1

    return decrypted

def main():
    choice = input('Encode or decode? ').lower()

    if choice == 'encode':
        message = input('Message to encode: ')
        passphrase = ''

        while not len(passphrase) == 4:
            passphrase = input('Passphrase (four characters): ')
        
        encrypted = encode(message, passphrase)
        print('Encoded message: ' + encrypted)
    
    elif choice == 'decode':
        message = input('Message to decode: ')
        passphrase = input('Passphrase (four characters): ')
        decrypted = decode(message, passphrase)
        print('Decoded message: ' + decrypted)

while True:
    main()