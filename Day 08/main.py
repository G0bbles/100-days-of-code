print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))


# def encrypt(message, shift):
#     encrypted_text = ''

#     for l in message:
#         if 97 <= ord(l) <= 122:
#             if ord(l) + shift > 122:
#                 encrypted_text += chr(shift - (123 - ord(l)) + 97)
#             else:
#                 encrypted_text += chr(shift + ord(l))

#         elif 65 <= ord(l) <= 90:
#             if ord(l) + shift > 90:
#                 encrypted_text += chr(shift - (91 - ord(l)) + 65)
#             else:
#                 encrypted_text += chr(shift + ord(l))
        
#         else:
#             encrypted_text += l
#     return encrypted_text

# print(encrypt("Hello z", 9))


def caesar(message, shift, encrypt_or_decrypt):
    cipher_text = ""

    if encrypt_or_decrypt.lower() == 'decrypt':
        shift *= -1

    for letter in message:
        if ord(letter) not in range(97, 123) and ord(letter) not in range(65,91):
            cipher_text += letter

        elif ord(letter) in range(97, 123) and \
            (97 > ord(letter) + shift or ord(letter) + shift > 122):
            alphabet_position = ord(letter) - 96
            new_position = (alphabet_position + shift) % 26
            cipher_text += chr(new_position + 96)

        elif ord(letter) in range(65, 91) and \
            (65 > ord(letter) + shift or ord(letter) + shift > 90):
            alphabet_position = ord(letter) - 64
            new_position = (alphabet_position + shift) % 26
            cipher_text += chr(new_position + 64)

        else:
            cipher_text += chr(ord(letter) + shift)

    return cipher_text

END_CIPHER = False
while not END_CIPHER:
    text = input("What is you message?\n")
    shift_amount = int(input("How many should I shift by?\n"))
    encrypt_or_decrypt = input("Do you want to 'encrypt' or 'decrypt'?\n")
    print(caesar(text, shift_amount, encrypt_or_decrypt))
    done = input("Would you like to continue? 'yes' or 'no'.\n").lower()
    
    if done == 'no':
        END_CIPHER = True
