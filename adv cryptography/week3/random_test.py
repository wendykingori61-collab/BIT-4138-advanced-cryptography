import random

def lfsr_generate(seed, taps, length):
    """Simple LFSR generator for testing"""
    state = [int(bit) for bit in seed]
    sequence = []
    
    for _ in range(length):
        feedback = 0
        for tap in taps:
            feedback ^= state[tap]
        state.pop()
        state.insert(0, feedback)
        sequence.append(feedback)
    
    return sequence

def frequency_test(sequence):
    """Test if number of 0s and 1s is approximately equal"""
    zeros = sequence.count(0)
    ones = sequence.count(1)
    total = len(sequence)
    
    zero_ratio = zeros / total
    one_ratio = ones / total
    
    print(f"   Zeros: {zeros} ({zero_ratio:.2%})")
    print(f"   Ones: {ones} ({one_ratio:.2%})")
    
    if 0.45 <= zero_ratio <= 0.55:
        print("   PASS: Good balance of bits")
    else:
        print("   WARNING: Unbalanced sequence")

def runs_test(sequence):
    """Test if runs of same bits are as expected"""
    runs = []
    current_run = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    
    print(f"   Number of runs: {len(runs)}")
    print(f"   Average run length: {sum(runs)/len(runs):.2f}")
    
    if 1.8 <= sum(runs)/len(runs) <= 2.2:
        print("   PASS: Run lengths appear random")
    else:
        print("   WARNING: Run length pattern detected")

print("=" * 60)
print("STATISTICAL RANDOMNESS TESTING")
print("=" * 60)

# Generate test sequences
print("\n--- GENERATING TEST SEQUENCES ---")

print("\n1. LFSR Sequence (500 bits):")
lfsr_seq = lfsr_generate("10101010", [0,3,4,7], 500)
print(f"   First 50 bits: {lfsr_seq[:50]}")

print("\n2. Python Random Sequence (500 bits):")
random_seq = [random.randint(0, 1) for _ in range(500)]
print(f"   First 50 bits: {random_seq[:50]}")

print("\n3. Alternating Pattern (010101... - NOT random):")
pattern_seq = [i % 2 for i in range(500)]
print(f"   First 50 bits: {pattern_seq[:50]}")

# Run tests
print("\n" + "=" * 60)
print("TEST RESULTS")
print("=" * 60)

print("\n--- LFSR Sequence ---")
print("Frequency Test:")
frequency_test(lfsr_seq)
print("\nRuns Test:")
runs_test(lfsr_seq)

print("\n--- Python Random Sequence ---")
print("Frequency Test:")
frequency_test(random_seq)
print("\nRuns Test:")
runs_test(random_seq)

print("\n--- Alternating Pattern ---")
print("Frequency Test:")
frequency_test(pattern_seq)
print("\nRuns Test:")
runs_test(pattern_seq)

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)
print("LFSR provides pseudorandom sequences for stream ciphers")
print("Patterns indicate weak randomness")
print("Cryptographic applications need unpredictable sequences")

