characters = ':€;”1p—)>{iÚ»Xu}rˇÔ`\uf8ff‡.B\'SUÏoZ¸⁄∏◊¯Cn¿]%tJQ#gbO?=ﬂ’h˜K"˛‰Ó˝MG@Ç+^vÎVc‹˘F4L9x2&E/¨kıf8\x07·±Œ[Íq°H›‚jˆ´lÆDÅ„Øﬁ6~I(<R!TeÒ$_Á0ysÂzY5N,wWPA*-d7m|3'

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