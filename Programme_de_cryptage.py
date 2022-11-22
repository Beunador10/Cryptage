def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ''
    
    return padded_key


def _encrypt_descrypt_char(plaintext_char, key_char, mode='encrypt'):
    
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'
            
        ord_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
        key_char_position = ord(key_char.lower()) - ord('a')
        
        if mode == 'encrypt' :
            new_char_position = (ord_char_position + key_char_position) % 26
        else :
            new_char_position = (ord_char_position - key_char_position + 26) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintext_char

def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
         ciphertext += _encrypt_descrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_descrypt_char(ciphertext_char, key_char, mode='decrypt')
    return plaintext

plaintext = input('Entrez le message a crypter :  ')
key = input('Entrez la cle: ')
# print(plaintext)
# print(key)

ciphertext = encrypt(plaintext, key)
# print(encrypt(plaintext, key))
decrypt_plaintext = decrypt(ciphertext, key)

print(f' Le texte crypté est : {ciphertext}') 
print(f'texte décrypté est : {decrypt_plaintext}')    

            