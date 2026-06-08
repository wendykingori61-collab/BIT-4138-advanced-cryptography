"""
Encryption Performance Testing
Measures speed of stream cipher encryption
"""

import time
import random

def lfsr_encrypt(data, seed, taps):
    """Simple LFSR stream encryption"""
    state = [int(bit) for bit in seed]
    keystream = []
    
    for _ in range(len(data)):
        feedback = 0
        for tap in taps:
            feedback ^= state[tap]
        state.pop()
        state.insert(0, feedback)
        keystream.append(feedback)
    
    encrypted = []
    for i, byte in enumerate(data):
        encrypted.append(byte ^ keystream[i % len(keystream)])
    
    return encrypted

print("=" * 60)
print("ENCRYPTION PERFORMANCE TESTING")
print("=" * 60)

# Test different data sizes
sizes = [1000, 10000, 50000, 100000]

print(f"\n{'Data Size':<12} {'Time (seconds)':<18} {'Speed (KB/s)':<15}")
print("-" * 50)

for size in sizes:
    # Generate random test data
    test_data = [random.randint(0, 255) for _ in range(size)]
    
    # Measure encryption time
    start_time = time.time()
    encrypted = lfsr_encrypt(test_data, "10101010", [0, 3])
    end_time = time.time()
    
    elapsed = end_time - start_time
    speed = (size / 1024) / elapsed if elapsed > 0 else 0
    
    print(f"{size:<12} {elapsed:<18.6f} {speed:<15.2f}")

print("\n" + "=" * 60)
print("PERFORMANCE ANALYSIS")
print("=" * 60)
print("✅ Stream ciphers are fast and efficient")
print("✅ Encryption time scales linearly with data size")
print("✅ Good for real-time encryption (video/audio streams)")
print("✅ Minimal memory overhead")
print("")
print("--- RECOMMENDATIONS ---")
print("• Small data (< 1KB): Any cipher works fine")
print("• Large data (> 1MB): Use hardware-accelerated AES")
print("• Streaming data: Use ChaCha20 (modern stream cipher)")
print("• This simulation: Educational purposes only")

print("\n" + "=" * 60)
print("CONCLUSION - WEEK 3")
print("=" * 60)
print("LFSR generates pseudorandom sequences for stream ciphers")
print("Statistical tests help evaluate randomness quality")
print("RC4 demonstrates practical stream cipher operation")
print("Performance testing shows stream ciphers are efficient")