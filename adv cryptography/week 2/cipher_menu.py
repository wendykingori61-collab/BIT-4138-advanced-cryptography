"""
Classical Cryptography Menu System
User Input Validation Interface
"""

def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher"""
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(plaintext, key):
    """Encrypt using Vigenère cipher"""
    ciphertext = ""
    key_length = len(key)
    key_as_int = [ord(k.lower()) - 97 for k in key]
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            p_int = ord(char.lower()) - 97
            k_int = key_as_int[i % key_length]
            encrypted_int = (p_int + k_int) % 26
            encrypted_char = chr(encrypted_int + 97)
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(k.lower()) - 97 for k in key]
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            c_int = ord(char.lower()) - 97
            k_int = key_as_int[i % key_length]
            decrypted_int = (c_int - k_int) % 26
            decrypted_char = chr(decrypted_int + 97)
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def validate_shift():
    """Validate shift input (1-25)"""
    while True:
        try:
            shift = int(input("Enter shift (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("❌ Shift must be between 1 and 25. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

def validate_key():
    """Validate key (alphabetic only)"""
    while True:
        key = input("Enter key (letters only): ")
        if key.isalpha():
            return key.lower()
        else:
            print("❌ Key must contain only letters. Try again.")

def main_menu():
    print("\n" + "=" * 50)
    print("CLASSICAL CRYPTOGRAPHY TOOL")
    print("=" * 50)
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Exit")
    print("=" * 50)

def caesar_menu():
    print("\n--- CAESAR CIPHER ---")
    message = input("Enter message: ")
    shift = validate_shift()
    
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    print(f"\nOriginal: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

def vigenere_menu():
    print("\n--- VIGENÈRE CIPHER ---")
    message = input("Enter message: ")
    key = validate_key()
    
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)
    
    print(f"\nOriginal: {message}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

# Main program
print("=" * 50)
print("WELCOME TO CLASSICAL CRYPTOGRAPHY TOOL")
print("=" * 50)

while True:
    main_menu()
    choice = input("\nSelect option (1-3): ")
    
    if choice == "1":
        caesar_menu()
    elif choice == "2":
        vigenere_menu()
    elif choice == "3":
        print("\nGoodbye! Thanks for using the Cryptography Tool.")
        break
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
    
    input("\nPress Enter to continue...")