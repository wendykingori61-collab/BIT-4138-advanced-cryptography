"""
AES Encryption Demonstration
Using Python's cryptography library
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

def generate_aes_key(password, salt):
    """Generate AES key from password using PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def aes_encrypt(plaintext, key):
    """Encrypt plaintext using AES-256 in CBC mode"""
    # Generate random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create AES cipher in CBC mode
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # Pad plaintext to multiple of 16 bytes (AES block size)
    padding_length = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext + chr(padding_length) * padding_length
    
    # Encrypt
    ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()
    
    # Return IV + ciphertext (base64 encoded for readability)
    result = base64.b64encode(iv + ciphertext).decode()
    return result

def aes_decrypt(encrypted_data, key):
    """Decrypt ciphertext using AES-256 in CBC mode"""
    # Decode from base64
    data = base64.b64decode(encrypted_data)
    
    # Extract IV (first 16 bytes) and ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Create AES cipher in CBC mode
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    
    # Decrypt
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove padding
    padding_length = padded_plaintext[-1]
    plaintext = padded_plaintext[:-padding_length].decode()
    
    return plaintext

print("=" * 60)
print("AES-256 ENCRYPTION DEMONSTRATION")
print("=" * 60)

# Generate a key from a password
password = "MyStrongPassword123!"
salt = os.urandom(16)

print(f"\nPassword: {password}")
print(f"Salt: {salt.hex()[:16]}...")

key = generate_aes_key(password, salt)
print(f"Generated AES-256 Key: {key.hex()[:16]}...")
print(f"Key length: {len(key)} bytes (256-bit)")

# Test encryption
print("\n" + "-" * 60)
print("ENCRYPTION TEST")
print("-" * 60)

original_message = "Hello AES! This is my secret message for Week 4."
print(f"Original: {original_message}")

encrypted = aes_encrypt(original_message, key)
print(f"Encrypted: {encrypted[:60]}...")

decrypted = aes_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

# Verify
if original_message == decrypted:
    print("\n✅ SUCCESS: Encryption and decryption working correctly!")
else:
    print("\n❌ ERROR: Decryption failed")

print("\n" + "=" * 60)
print("AES FEATURES")
print("=" * 60)
print("✅ Block cipher (128-bit blocks)")
print("✅ Symmetric encryption (same key for encrypt/decrypt)")
print("✅ CBC mode with random IV for semantic security")
print("✅ AES-256 provides 256-bit key strength")
print("✅ Industry standard for secure encryption")
