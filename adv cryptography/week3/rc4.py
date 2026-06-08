"""
RC4 Stream Cipher Simulation
"""

def rc4_encrypt(data, key):
    """Encrypt/decrypt data using RC4"""
    if isinstance(key, str):
        key = [ord(c) for c in key]
    if isinstance(data, str):
        data = [ord(c) for c in data]
    
    # Initialize S-box
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Generate keystream and encrypt
    result = []
    i = 0
    j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(byte ^ K)
    
    return result

def bytes_to_string(byte_list):
    """Convert bytes back to string"""
    return ''.join(chr(b) for b in byte_list)

print("=" * 60)
print("RC4 STREAM CIPHER SIMULATION")
print("=" * 60)

# Test 1: Basic encryption
print("\n--- Test 1: Basic Encryption/Decryption ---")
message = "Hello World!"
key = "SecretKey"

print(f"Original: {message}")
print(f"Key: {key}")

encrypted = rc4_encrypt(message, key)
decrypted = rc4_encrypt(encrypted, key)

print(f"Encrypted (bytes): {encrypted}")
print(f"Decrypted: {bytes_to_string(decrypted)}")

# Test 2: Different key produces different output
print("\n--- Test 2: Different Key = Different Ciphertext ---")
message2 = "SECRET MESSAGE"
key1 = "Key123"
key2 = "Key456"

encrypted1 = rc4_encrypt(message2, key1)
encrypted2 = rc4_encrypt(message2, key2)

print(f"Message: {message2}")
print(f"With key '{key1}': {encrypted1[:10]}...")
print(f"With key '{key2}': {encrypted2[:10]}...")
print("Different keys produce completely different ciphertext")

# Test 3: Same message different keys
print("\n--- Test 3: Same Message, Different Keys ---")
msg = "AAAAA"
enc_with_key1 = rc4_encrypt(msg, "KEY1")
enc_with_key2 = rc4_encrypt(msg, "KEY2")
print(f"Message: {msg}")
print(f"With KEY1: {enc_with_key1}")
print(f"With KEY2: {enc_with_key2}")

print("\n" + "=" * 60)
print("RC4 ANALYSIS")
print("=" * 60)
print("✅ Fast stream cipher - good for streaming data")
print("✅ Symmetric encryption - same function for encrypt/decrypt")
print("❌ Has biases in keystream (first few bytes predictable)")
print("❌ Considered broken - not recommended for new applications")
print("✅ Modern alternative: ChaCha20")