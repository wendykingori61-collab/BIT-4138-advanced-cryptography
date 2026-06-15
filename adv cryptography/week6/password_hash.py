"""
Password Hashing and Authentication System
"""

import hashlib
import os
import binascii

def hash_password(password):
    """Hash a password with a random salt"""
    salt = os.urandom(16)
    password_bytes = password.encode()
    hash_object = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    password_hash = binascii.hexlify(hash_object).decode()
    salt_hex = binascii.hexlify(salt).decode()
    return salt_hex, password_hash

def verify_password(password, salt_hex, stored_hash):
    """Verify a password against stored salt and hash"""
    salt = binascii.unhexlify(salt_hex)
    password_bytes = password.encode()
    hash_object = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    computed_hash = binascii.hexlify(hash_object).decode()
    return computed_hash == stored_hash

print("=" * 60)
print("PASSWORD HASHING SYSTEM")
print("=" * 60)

# User registration
user_database = {}

print("\n--- USER REGISTRATION ---")
username = "alice"
password = "MySecurePassword123!"

salt, password_hash = hash_password(password)
user_database[username] = {"salt": salt, "hash": password_hash}

print(f"Username: {username}")
print(f"Password: {password}")
print(f"Salt (first 32 chars): {salt[:32]}...")
print(f"Password Hash (first 32 chars): {password_hash[:32]}...")
print("\n✅ Password securely stored with salt")
print("   (Plaintext password NEVER stored!)")

print("\n" + "=" * 60)
print("LOGIN AUTHENTICATION WORKFLOW")
print("=" * 60)

# Successful login
print("\n--- LOGIN ATTEMPT 1: Correct Password ---")
attempt = "MySecurePassword123!"

if verify_password(attempt, user_database[username]["salt"], user_database[username]["hash"]):
    print("✅ LOGIN SUCCESSFUL! Password verified.")
else:
    print("❌ LOGIN FAILED! Incorrect password.")

# Failed login
print("\n--- LOGIN ATTEMPT 2: Wrong Password ---")
attempt = "WrongPassword"

if verify_password(attempt, user_database[username]["salt"], user_database[username]["hash"]):
    print("✅ LOGIN SUCCESSFUL! Password verified.")
else:
    print("❌ LOGIN FAILED! Incorrect password.")

print("\n" + "=" * 60)
print("SECURITY FEATURES")
print("=" * 60)
print("✅ Passwords never stored in plaintext")
print("✅ Unique random salt for each password")
print("✅ Same password = different hashes (due to salt)")
print("✅ PBKDF2 slows down brute force attacks")