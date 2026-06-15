def caesar_encrypt(text, shift):
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
    return caesar_encrypt(text, -shift)

print("=" * 50)
print("CAESAR CIPHER DEMONSTRATION")
print("=" * 50)

message = input("Enter message to encrypt: ")
shift = int(input("Enter shift value (1-25): "))

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"\nOriginal: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

print("\n--- SECURITY ANALYSIS ---")
print("Caesar Cipher weakness: Only 25 possible shifts")
print("Vulnerable to brute force attack")