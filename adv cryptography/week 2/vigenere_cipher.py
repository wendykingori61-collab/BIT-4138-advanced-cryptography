def vigenere_encrypt(plaintext, key):
    """Encrypt using Vigenère cipher"""
    ciphertext = ""
    key_length = len(key)
    key_as_int = [ord(k.lower()) - 97 for k in key]
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Convert letter to number (0-25)
            p_int = ord(char.lower()) - 97
            k_int = key_as_int[i % key_length]
            encrypted_int = (p_int + k_int) % 26
            encrypted_char = chr(encrypted_int + 97)
            
            # Preserve original case
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            
            ciphertext += encrypted_char
        else:
            # Keep non-letters as is
            ciphertext += char
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypt using Vigenère cipher"""
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(k.lower()) - 97 for k in key]
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            # Convert letter to number (0-25)
            c_int = ord(char.lower()) - 97
            k_int = key_as_int[i % key_length]
            decrypted_int = (c_int - k_int) % 26
            decrypted_char = chr(decrypted_int + 97)
            
            # Preserve original case
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            
            plaintext += decrypted_char
        else:
            # Keep non-letters as is
            plaintext += char
    
    return plaintext

# Demonstration
print("=" * 50)
print("VIGENÈRE CIPHER DEMONSTRATION")
print("=" * 50)

message = input("Enter message to encrypt: ")
key = input("Enter encryption key (letters only): ")

encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)

print(f"\nOriginal: {message}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

print("\n--- SECURITY ANALYSIS ---")
print("✅ Vigenère is stronger than Caesar (polyalphabetic)")
print("✅ Same letter can encrypt to different letters")
print("⚠️ Still vulnerable to Kasiski analysis if key is short")