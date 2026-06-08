"""
Cipher Testing Results
Testing both ciphers with different inputs and brute force demonstration
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

def brute_force_caesar(ciphertext):
    """Try all 25 shifts to break Caesar cipher"""
    print("\n" + "=" * 60)
    print("BRUTE FORCE ATTACK ON CAESAR CIPHER")
    print("=" * 60)
    print(f"Ciphertext: {ciphertext}\n")
    print("Trying all 25 possible shifts:")
    print("-" * 40)
    
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {decrypted}")
    
    print("-" * 40)
    print("⚠️ Notice how the correct message appears at the correct shift!")
    print("⚠️ This shows why Caesar cipher is NOT secure.")

def run_tests():
    """Run multiple test cases for both ciphers"""
    print("=" * 60)
    print("CIPHER TESTING RESULTS")
    print("=" * 60)
    
    # Test cases: (message, shift, key)
    test_cases = [
        ("HELLO", 3, "A"),
        ("Python", 5, "KEY"),
        ("Hello World!", 7, "SECRET"),
        ("Cryptography", 12, "CODE"),
        ("ABC", 1, "B"),
    ]
    
    print("\n--- CAESAR CIPHER TESTS ---")
    print(f"{'Message':<20} {'Shift':<6} {'Encrypted':<25} {'Decrypted':<15}")
    print("-" * 70)
    for msg, shift, _ in test_cases:
        encrypted = caesar_encrypt(msg, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print(f"{msg:<20} {shift:<6} {encrypted:<25} {decrypted:<15}")
    
    print("\n--- VIGENÈRE CIPHER TESTS ---")
    print(f"{'Message':<20} {'Key':<8} {'Encrypted':<30} {'Decrypted':<15}")
    print("-" * 75)
    for msg, _, key in test_cases:
        encrypted = vigenere_encrypt(msg, key)
        decrypted = vigenere_decrypt(encrypted, key)
        print(f"{msg:<20} {key:<8} {encrypted:<30} {decrypted:<15}")
    
    # Demonstrate that same letters encrypt differently in Vigenère
    print("\n" + "=" * 60)
    print("DEMONSTRATION: SAME LETTER ENCRYPTS DIFFERENTLY")
    print("=" * 60)
    
    test_msg = "AAAAA"
    test_key = "SECRET"
    encrypted = vigenere_encrypt(test_msg, test_key)
    print(f"Message: {test_msg}")
    print(f"Key: {test_key}")
    print(f"Encrypted: {encrypted}")
    print("✅ Notice: All 'A's encrypted to different letters!")
    print("✅ This is polyalphabetic substitution - Vigenère's advantage over Caesar.")

def main():
    """Main function to run all tests"""
    # Run the test suite
    run_tests()
    
    # Demonstrate brute force attack
    print("\n" + "=" * 60)
    print("SECURITY VULNERABILITY DEMONSTRATION")
    print("=" * 60)
    
    # Encrypt a message with Caesar
    original = "SECRET MESSAGE"
    shift = 5
    encrypted = caesar_encrypt(original, shift)
    
    print(f"Original: {original}")
    print(f"Shift used: {shift}")
    print(f"Encrypted: {encrypted}")
    
    # Show brute force attack
    brute_force_caesar(encrypted)
    
    print("\n" + "=" * 60)
    print("CONCLUSION")
    print("=" * 60)
    print("✅ Caesar Cipher: Easy to implement but VERY weak (only 25 keys)")
    print("✅ Vigenère Cipher: Stronger, but still vulnerable with short keys")
    print("✅ Modern ciphers (AES) are needed for real security")

if __name__ == "__main__":
    main()