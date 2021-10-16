def c_cipher(text, shift):
    ciphered = ''
    for c in text:
        if c.isupper():
            ciphered += chr((ord(c) + shift - 65) % 26 + 65)
        elif c.islower():
            ciphered += chr((ord(c) + shift - 97) % 26 + 97)
        else:
            ciphered += c
    return ciphered


def d_cipher(text, shift):
    d_ciphered = ''
    for c in text:
        if c.isupper():
            d_ciphered += chr((ord(c) - shift - 65) % 26 + 65)
        elif c.islower():
            d_ciphered += chr((ord(c) - shift - 97) % 26 + 97)
        else:
            d_ciphered += c
    return d_ciphered


