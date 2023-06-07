def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Example:
plaintext = "HELLO WORLD"
key = 3

encrypted_text = caesar_cipher_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
