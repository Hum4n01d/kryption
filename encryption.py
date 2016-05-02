characters = '#c9f:nrb3pl/o<?G4^%F,V(}T~uQ$ghCÑ5&.eHj2LJd!¥€+ RkI[y>{S"]X@MK)OW\\wBa|vY681q7D£;=N-EiAzmP0UZ\'sx*t_•'

characters_length = len(characters)

def encode(message, passphrase):
    encrypted = ''
    counter = 0
    
    for char in message:
        print('Char: ' + char)
        
        char_index = characters.index(char)
        print('Char index: ' + str(char_index))
		
        print('Counter: ' + str(counter))
        
        passphrase_char = passphrase[counter]
        print('Passphrase char: ' + passphrase_char)
        
        counter_char_index = characters.index(passphrase_char)
        print('Counter char index: ' + str(counter_char_index))
		
        together = char_index + counter_char_index
        print('Together: ' + str(together))
		
        modded =  together % characters_length
        print('Modded: ' + str(modded))
        
        encrypted += characters[modded]
        
        if counter == len(passphrase) -1:
            counter = 0
        else:
            counter += 1

    return encrypted

def decode(message, passphrase):
    decrypted = ''

    counter = 0
    
    for char in message:
        print('Char: ' + char)
        
        char_index = characters.index(char)
        print('Char index: ' + str(char_index))
		
        print('Counter: ' + str(counter))
        
        passphrase_char = passphrase[counter]
        print('Passphrase char: ' + passphrase_char)
        
        counter_char_index = characters.index(passphrase_char)
        print('Counter char index: ' + str(counter_char_index))
		
        together = char_index - counter_char_index
        print('Together: ' + str(together))
		
        modded =  together % characters_length
        print('Modded: ' + str(modded))
        
        decrypted += characters[modded]
        
        if counter == len(passphrase) -1:
            counter = 0
        else:
            counter += 1

    return decrypted