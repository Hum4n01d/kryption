from os import system
system('clear')

# All encodable characters
letters = '''qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890-/:;()$&@".,?!'[]{}#%^*+=_\|~<>€£¥• '''

# Encode mesage
def encode(message, key):
    encrypted = ''
    counter = 0
    for char in message:
        # Add the index of the character in the characters variable, add 100 (so that all codes are three digit), then add the key for extra security
        
        if key > 99:
            if counter == 0:
                encrypted += str(letters.index(char) + key + 1)
            elif counter == 1:
                encrypted += str(letters.index(char) + key + 3)
            elif counter == 2:
                encrypted += str(letters.index(char) + key + 3)
            elif counter == 3:
                encrypted += str(letters.index(char) + key + 7)
        else:
            if counter == 0:
                encrypted += str(letters.index(char) + 100 + key + 1)
            elif counter == 1:
                encrypted += str(letters.index(char) + 100 + key + 3)
            elif counter == 2:
                encrypted += str(letters.index(char) + 100 + key + 3)
            elif counter == 3:
                encrypted += str(letters.index(char) + 100 + key + 7)
        
        if counter > 3:
          counter = 0
        else:
          counter += 1
        

    return encrypted

# Decode message
def decode(message, key):
    decrypted = ''

    counter = 0
    counter2 = 0
    
    for (index, char) in enumerate(message):
        # Counter used to skip two every time because the number only means something when it's 3 digits
        if counter == 0:
          
            # This is true for every third number
            # Get the next two characters as well and add them as a string to the num variable
            num = char + str(message[index + 1]) + str(message[index + 2])

            # Get the character at the index by reversing the extra operations done in encoding
            if key > 99:
                if counter2 == 0:
                  decrypted += letters[int(num) - key - 1]
                elif counter2 == 1:
                    decrypted += letters[int(num) - key - 3]
                elif counter2 == 2:
                    decrypted += letters[int(num) - key - 3]
                elif counter2 == 3:
                    decrypted += letters[int(num) - key - 7]
            else:
                if counter2 == 0:
                    decrypted += letters[int(num) - 100 - key - 1]
                elif counter2 == 1:
                    decrypted += letters[int(num) - 100 - key - 3]
                elif counter2 == 2:
                    decrypted += letters[int(num) - 100 - key - 3]
                elif counter2 == 3:
                    decrypted += letters[int(num) - 100 - key - 7]
                

            counter = 1
        else:
            # Logic for the counter
            if counter == 2:
                counter = 0
            else:
                counter += 1
                
        if counter2 > 3:
          counter2 = 0
        else:
          counter2 += 1

    return decrypted

# Main loop
def main():
    # Get user choice (encode or decode)
    choice = input('Encode or decode? ').lower()

    if choice == 'encode':
        # Get message and key that is between 0 and 794 because if the key is bigger, there could be a character encoded as 4 digits which would break the decoding program
        message = input('Message to encode: ')
        key = -1

        while key < 0 or key > 999:
            key = int(input('Passkey (3 digit int): '))
        
        encrypted = encode(message, key)
        print('Encoded message: ' + encrypted)
    
    elif choice == 'decode':
        message = input('Message to decode: ')
        key = int(input('Passkey (int): '))
        decrypted = decode(message, key)
        print('Decoded message: ' + decrypted)

while True:
    main()