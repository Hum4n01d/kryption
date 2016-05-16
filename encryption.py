# -*- coding: utf-8 -*-

characters = '#c9f:nrb3pl/o<?G4^%F,V(}T~uQ$ghCÑ5&.eHj2LJd!¥€+ RkI[y>{S"]X@MK)OW\\wBa|vY681q7D£;=N-EiAzmP0UZ\'sx*t_•'

characters_length = len(characters)

def encode(message, passphrase):
    encrypted = ''
    counter = 0
    
    for char in message:
        char_index = characters.index(char)
        passphrase_char = passphrase[counter]
        counter_char_index = characters.index(passphrase_char)
        together = char_index + counter_char_index
        modded =  together % characters_length
        
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
        char_index = characters.index(char)
        passphrase_char = passphrase[counter]
        counter_char_index = characters.index(passphrase_char)
        together = char_index - counter_char_index
        modded =  together % characters_length
        
        decrypted += characters[modded]
        
        if counter == len(passphrase) -1:
            counter = 0
        else:
            counter += 1

    return decrypted