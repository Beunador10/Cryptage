def detail_cle(texte_clair, cle):
    cle_detail = ''
    i = 0
    for char in texte_clair:
        if char.isalpha():
            cle_detail += cle[i % len(cle)]
            i += 1
        else:
            cle_detail += ''
    
    return cle_detail


def encrypt_descrypt_char(texte_clair_char, cle_char, mode='encrypt'):
    
    if texte_clair_char.isalpha():
        premiere_lettre_alphabet = 'a'
        if texte_clair_char.isupper():
            premiere_lettre_alphabet = 'A'
            
        texte_char_position = ord(texte_clair_char) - ord(premiere_lettre_alphabet)
        cle_char_position = ord(cle_char.lower()) - ord('a')
        
        if mode == 'encrypt' :
            new_char_position = (texte_char_position + cle_char_position) % 26
        else :
            new_char_position = (texte_char_position - cle_char_position + 26) % 26
        return chr(new_char_position + ord(premiere_lettre_alphabet))
    return texte_clair_char

def encrypt(texte_clair, cle):
    text_chiffre = ''
    cle_remboure = detail_cle(texte_clair, cle)
    for texte_clair_char, cle_char in zip(texte_clair, cle_remboure):
         text_chiffre += encrypt_descrypt_char(texte_clair_char, cle_char)
    return text_chiffre

def decrypt(texte_chiffre, cle):
    texte_clair = ''
    cle_remboure = detail_cle(texte_chiffre, cle)
    for texte_chiffre_char, cle_char in zip(texte_chiffre, cle_remboure):
        texte_clair += encrypt_descrypt_char(texte_chiffre_char, cle_char, mode='decrypt')
    return texte_clair

texte_clair = input('Entrez le message a crypter :  ')
cle = input('Entrez la cle: ')
# print(texte_clair)
# print(cle)

texte_chiffre = encrypt(texte_clair, cle)
# print(encrypt(texte_clair, cle))
texte_decrypte = decrypt(texte_chiffre, cle)

print(f' Le texte crypté est : {texte_chiffre}') 
print(f' Le texte décrypté est : {texte_decrypte}')    

            