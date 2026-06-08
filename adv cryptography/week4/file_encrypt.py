"""
File Encryption and Decryption with AES
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(input_file, output_file, key):
    """Encrypt a file using AES-256"""
    iv = os.urandom(16)
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Add PKCS7 padding
    pad_length = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext + bytes([pad_length] * pad_length)
    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)
    
    print(f"File encrypted: {input_file} -> {output_file}")
    print(f"   Original size: {len(plaintext)} bytes")
    print(f"   Encrypted size: {len(iv + ciphertext)} bytes")

def decrypt_file(input_file, output_file, key):
    """Decrypt a file using AES-256"""
    with open(input_file, 'rb') as f:
        data = f.read()
    
    iv = data[:16]
    ciphertext = data[16:]
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove PKCS7 padding
    pad_length = padded_plaintext[-1]
    plaintext = padded_plaintext[:-pad_length]
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print(f"File decrypted: {input_file} -> {output_file}")

print("=" * 60)
print("AES FILE ENCRYPTION DEMONSTRATION")
print("=" * 60)

# Create a test file
test_content = "This is a secret file content for AES encryption testing.\n" * 10
with open("test_secret.txt", "w") as f:
    f.write(test_content)

print("\nCreated test file: test_secret.txt")
print("Content preview:")
print(test_content[:100] + "...")

# Generate a key
key = os.urandom(32)  # 32 bytes = AES-256
print(f"\nGenerated AES-256 key: {key.hex()[:32]}...")

# Encrypt the file
print("\n--- ENCRYPTING FILE ---")
encrypt_file("test_secret.txt", "test_secret.enc", key)

# Decrypt the file
print("\n--- DECRYPTING FILE ---")
decrypt_file("test_secret.enc", "test_secret_decrypted.txt", key)

# Verify
print("\n--- VERIFICATION ---")
with open("test_secret.txt", "r") as f:
    original = f.read()
with open("test_secret_decrypted.txt", "r") as f:
    decrypted = f.read()

if original == decrypted:
    print("SUCCESS: File encryption/decryption verified!")
    print("Decrypted file matches the original exactly.")
else:
    print("ERROR: Files don't match")

print("\n" + "=" * 60)
print("FILE ENCRYPTION FEATURES")
print("=" * 60)
print("Encrypts any file type (text, images, documents)")
print("Preserves data integrity")
print("Uses IV for unique ciphertext each time")
print("Industry standard for file protection")