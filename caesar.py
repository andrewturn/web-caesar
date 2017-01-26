def encrypt(text, rot):
    encrypted = ''
    for a_letter in text:
        rotate_character(a_letter, rot)
        encrypted = encrypted + rotate_character(a_letter, rot)
    return encrypted

def alphabet_position(letter):
    a_char = letter
    for a_char in letter:
        if a_char.isalpha() == True:
            a_char = ord(a_char)
        if a_char >= 97 and a_char <= 122:
            a_lower = a_char - 97
            return a_lower
        elif a_char >= 65 and a_char <= 90:
                a_upper = a_char - 65
                return a_upper


def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    if char.isalpha() == False:
        return char
    rotated_index = alphabet_position(char) + rot
    was_upper = char.isupper()
    alpha_char = char.isalpha()

    if rotated_index < 26:
        encrypted = encrypted + alphabet[rotated_index]
    else:
        encrypted = encrypted + alphabet[rotated_index % 26]
    if was_upper:
        encrypted = encrypted.upper()
    return encrypted
