"""
RSA Public Key Cryptography Demonstration
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption
import base64

def generate_rsa_keys():
    """Generate RSA public and private key pair"""
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,  # 2048-bit RSA is secure
    )
    
    # Get public key from private key
    public_key = private_key.public_key()
    
    return private_key, public_key

def encrypt_rsa(message, public_key):
    """Encrypt message using RSA public key"""
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
    """Decrypt message using RSA private key"""
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
print("RSA PUBLIC KEY CRYPTOGRAPHY DEMONSTRATION")
print("=" * 60)

# Generate key pair
print("\n--- STEP 1: RSA KEY PAIR GENERATION ---")
private_key, public_key = generate_rsa_keys()

# Get key numbers for display
private_numbers = private_key.private_numbers()
public_numbers = public_key.public_numbers()

print(f"RSA Key Size: 2048 bits")
print(f"Public Key (modulus n): {str(public_numbers.n)[:50]}...")
print(f"Public Key (exponent e): {public_numbers.e}")
print(f"Private Key (exponent d): {str(private_numbers.d)[:50]}...")

print("\n" + "=" * 60)
print("RSA KEY FEATURES")
print("=" * 60)
print("✅ Public key: Used for encryption (shared openly)")
print("✅ Private key: Used for decryption (kept secret)")
print("✅ Mathematically linked (RSA algorithm)")
print("✅ 2048-bit keys provide strong security")

print("\n" + "=" * 60)
print("STEP 2 & 3: ENCRYPTION & DECRYPTION")
print("=" * 60)

# Test message
message = "Hello RSA! This is my secret message for Week 5."
print(f"\nOriginal Message: {message}")

# Encrypt with public key
encrypted = encrypt_rsa(message, public_key)
print(f"\nEncrypted (Public Key): {encrypted[:60]}...")

# Decrypt with private key
decrypted = decrypt_rsa(encrypted, private_key)
print(f"Decrypted (Private Key): {decrypted}")

# Verify
if message == decrypted:
    print("\n✅ SUCCESS: RSA encryption and decryption working correctly!")
else:
    print("\n❌ ERROR: Decryption failed")

print("\n" + "=" * 60)
print("RSA SECURITY ANALYSIS")
print("=" * 60)
print("✅ Asymmetric encryption (different keys for encrypt/decrypt)")
print("✅ Public key can be shared openly")
print("✅ Private key must remain secret")
print("⚠️ Slower than symmetric encryption (AES)")
print("✅ Used for key exchange and digital signatures")
