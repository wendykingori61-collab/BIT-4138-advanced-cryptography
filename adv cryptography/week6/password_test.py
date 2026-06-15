"""
Password Security Testing
Testing different password strengths and hash verification
"""

import hashlib
import os
import time
import binascii

def hash_with_cost(password, iterations):
    """Hash password with configurable iterations"""
    salt = os.urandom(16)
    start = time.time()
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    elapsed = time.time() - start
    return elapsed, binascii.hexlify(hash_object).decode()[:32]

print("=" * 60)
print("PASSWORD SECURITY TESTING")
print("=" * 60)

# Test different password strengths
print("\n--- PASSWORD STRENGTH TEST ---")
passwords = [
    "123456",
    "password",
    "Pass123",
    "MyP@ssw0rd!",
    "C0mpl3x!S3cur3P@ss"
]

for pwd in passwords:
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    
    if has_upper and has_lower and has_digit and has_special and len(pwd) >= 12:
        rating = "VERY STRONG ✅✅✅"
    elif has_upper and has_lower and has_digit and len(pwd) >= 8:
        rating = "STRONG ✅✅"
    elif len(pwd) >= 6:
        rating = "MEDIUM ✅"
    else:
        rating = "WEAK ⚠️"
    
    print(f"\nPassword: '{pwd}'")
    print(f"  Length: {len(pwd)}")
    print(f"  Has uppercase: {has_upper}")
    print(f"  Has lowercase: {has_lower}")
    print(f"  Has digit: {has_digit}")
    print(f"  Has special: {has_special}")
    print(f"  Strength: {rating}")

print("\n" + "=" * 60)
print("HASHING COST DEMONSTRATION")
print("=" * 60)

password = "test123"
iterations_list = [1000, 10000, 50000, 100000]

print(f"\nPassword: '{password}'")
print("\nIterations    Time (seconds)")
print("-" * 35)

for iterations in iterations_list:
    elapsed, hash_val = hash_with_cost(password, iterations)
    print(f"{iterations:<12} {elapsed:.4f}")

print("\n" + "=" * 60)
print("SECURITY RECOMMENDATIONS")
print("=" * 60)
print("✅ Use passwords at least 12 characters long")
print("✅ Include uppercase, lowercase, numbers, and symbols")
print("✅ Never reuse passwords across sites")
print("✅ Use a password manager")
print("✅ Enable Two-Factor Authentication (2FA)")
print("\n❌ NEVER:")
print("   - Use dictionary words")
print("   - Use personal info (birthdays, names)")
print("   - Share passwords")
print("   - Write passwords down")

print("\n" + "=" * 60)
print("WEEK 6 COMPLETE")
print("=" * 60)
