from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
print(f"Generated Key: {key}")

# Create cipher object using the key
cipher = Fernet(key)

# Original message to encrypt
message = b"Hello Cryptography - Week 1 Setup Complete!"
print(f"\nOriginal Message: {message}")

# Encrypt the message
encrypted = cipher.encrypt(message)
print(f"Encrypted Message: {encrypted}")

# Decrypt the message back
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted Message: {decrypted.decode()}")

print("\n✅ SUCCESS: Cryptography is working correctly!")