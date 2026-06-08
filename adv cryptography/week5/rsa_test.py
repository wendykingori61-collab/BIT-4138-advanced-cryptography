"""
RSA Testing and Validation
Tests RSA with different message sizes
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64
import time

def encrypt_rsa(message, public_key):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()

def decrypt_rsa(ciphertext_b64, private_key):
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

print("=" * 60)
print("RSA TESTING AND VALIDATION")
print("=" * 60)

# Generate keys
private_key, public_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
), None
private_key_temp = rsa.generate_private_key(public_exponent=65537, key_size=2048)
private_key = private_key_temp
public_key = private_key.public_key()

print(f"\nRSA Key Size: 2048 bits")
print(f"Maximum message size: 190 bytes (with OAEP padding)")

# Test messages of different lengths
test_messages = [
    "A",
    "Hello RSA",
    "This is a longer test message for RSA encryption",
    "RSA is widely used for secure key exchange and digital signatures"
]

print("\n" + "=" * 60)
print("ENCRYPTION/DECRYPTION TESTS")
print("=" * 60)

for i, msg in enumerate(test_messages, 1):
    print(f"\n--- Test {i} ---")
    print(f"Message: {msg}")
    print(f"Length: {len(msg)} bytes")
    
    encrypted = encrypt_rsa(msg, public_key)
    decrypted = decrypt_rsa(encrypted, private_key)
    
    print(f"Encrypted (first 30 chars): {encrypted[:30]}...")
    print(f"Decrypted: {decrypted}")
    
    if msg == decrypted:
        print("✅ PASS")
    else:
        print("❌ FAIL")

print("\n" + "=" * 60)
print("RSA vs AES COMPARISON")
print("=" * 60)
print("RSA (Asymmetric):")
print("  • Uses public/private key pair")
print("  • Slower (1000x slower than AES)")
print("  • Used for key exchange, digital signatures")
print("  • Maximum message size limited by key size")
print("\nAES (Symmetric):")
print("  • Uses single shared key")
print("  • Very fast")
print("  • Used for bulk data encryption")
print("  • No message size limit")
print("\n✅ Best practice: Use RSA to encrypt AES key,")
print("   then use AES for actual data encryption")

print("\n" + "=" * 60)
print("WEEK 5 COMPLETE")
print("=" * 60)
print("✅ RSA key pair generated")
print("✅ Public key encryption working")
print("✅ Private key decryption working")
print("✅ Secure message transmission simulated")
print("✅ RSA testing completed")