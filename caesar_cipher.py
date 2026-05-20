# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_message = encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)
