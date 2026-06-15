"""
SHA-256 Hash Generation Demonstration
"""

import hashlib
import binascii

def generate_sha256(message):
    """Generate SHA-256 hash of a message"""
    # Convert message to bytes and hash
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()

print("=" * 60)
print("SHA-256 HASH GENERATION")
print("=" * 60)

# Test messages
messages = [
    "Hello World",
    "Hello World",  # Same message - same hash
    "Hello World!", # Different message - completely different hash
    "password123",
    "MySecretPassword"
]

print("\n--- SHA-256 HASH DEMONSTRATION ---")
print("\nNotice: Same message = same hash")
print("Different message = completely different hash\n")

for msg in messages:
    hash_value = generate_sha256(msg)
    print(f"Message: '{msg}'")
    print(f"SHA-256: {hash_value}")
    print("-" * 60)

print("\n--- PROPERTIES OF HASH FUNCTIONS ---")
print("✅ Same input always produces same hash (deterministic)")
print("✅ Different inputs produce completely different hashes")
print("✅ Cannot reverse hash to get original message (one-way)")
print("✅ Even tiny change produces entirely different hash")
print("✅ Fixed output length (64 characters for SHA-256)")

# Show avalanche effect
print("\n--- AVALANCHE EFFECT DEMONSTRATION ---")
msg1 = "Hello"
msg2 = "Hello"  # Same
msg3 = "Hell0"  # Changed 'o' to '0' (one character difference)

hash1 = generate_sha256(msg1)
hash3 = generate_sha256(msg3)

print(f"Message 1: '{msg1}'")
print(f"Hash 1: {hash1}")
print(f"\nMessage 3: '{msg3}'")
print(f"Hash 3: {hash3}")
print(f"\nOne character change = Completely different hash!")
print(f"✅ This is called the AVALANCHE EFFECT")
