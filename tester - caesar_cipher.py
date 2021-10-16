import caesar_cipher

print("Welcome to Caesar-Cipher++")

cmd = input("Do you want to encrypt or decrypt your text? Please indicate with e or d: ")

t = input("Please enter your text: ")


if cmd == 'e':
    s = int(input("Please type in the amount by which you want to shift: "))
    new_t = caesar_cipher.c_cipher(t, s)
    print(new_t)
else:
    s = int(input("Please type in the amount by which text was shifted: "))
    new_t = caesar_cipher.d_cipher(t, s)
    print(new_t)
