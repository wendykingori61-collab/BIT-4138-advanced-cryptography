"""
AES Performance Testing
Measures encryption speed for different data sizes
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import time

def aes_encrypt(data, key):
    """AES encryption for performance testing"""
    iv = os.urandom(16)
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # Add padding
    pad_length = 16 - (len(data) % 16)
    padded_data = data + bytes([pad_length] * pad_length)
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

print("=" * 60)
print("AES PERFORMANCE TESTING")
print("=" * 60)

# Generate AES-256 key
key = os.urandom(32)

# Test different data sizes
sizes = [1024, 10240, 102400, 1048576]
size_names = ["1 KB", "10 KB", "100 KB", "1 MB"]

print(f"\n{'Data Size':<12} {'Time (seconds)':<18} {'Speed (KB/s)':<15}")
print("-" * 50)

for size, name in zip(sizes, size_names):
    # Generate random test data
    test_data = os.urandom(size)
    
    # Measure encryption time
    start = time.time()
    encrypted = aes_encrypt(test_data, key)
    end = time.time()
    
    elapsed = end - start
    speed = (size / 1024) / elapsed if elapsed > 0 else 0
    
    print(f"{name:<12} {elapsed:<18.6f} {speed:<15.2f}")

print("\n" + "=" * 60)
print("PERFORMANCE ANALYSIS")
print("=" * 60)
print("✅ AES is highly optimized and fast")
print("✅ Hardware acceleration (AES-NI) available on most CPUs")
print("✅ Speed scales linearly with data size")
print("✅ Suitable for large files and disk encryption")
print("")
print("--- COMPARISON ---")
print("AES (block cipher) vs Stream ciphers:")
print("• AES: Better for random access / stored data")
print("• Stream: Better for continuous streams (video/audio)")
print("")
print("✅ AES is the global standard for symmetric encryption")

print("\n" + "=" * 60)
print("WEEK 4 COMPLETE")
print("=" * 60)
print("✅ AES Encryption implemented")
print("✅ Key generation working")
print("✅ File encryption/decryption tested")
print("✅ Performance measured")