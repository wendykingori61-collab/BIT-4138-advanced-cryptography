"""
Linear Feedback Shift Register (LFSR) Generator
Produces pseudorandom bit sequences for stream ciphers
"""

class LFSR:
    def __init__(self, seed, taps):
        """
        Initialize LFSR
        seed: initial state (binary string like '1010')
        taps: feedback positions (list of indices, 0-indexed from left)
        """
        self.state = [int(bit) for bit in seed]
        self.taps = taps
        self.initial_state = self.state.copy()
        self.bit_count = 0
    
    def next_bit(self):
        """Generate next bit and shift register"""
        # Calculate feedback bit (XOR of tap positions)
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        
        # Shift all bits right and insert feedback at beginning
        self.state.pop()
        self.state.insert(0, feedback)
        self.bit_count += 1
        
        return feedback
    
    def generate_sequence(self, length):
        """Generate sequence of bits"""
        sequence = []
        for _ in range(length):
            sequence.append(self.next_bit())
        return sequence
    
    def reset(self):
        """Reset to initial state"""
        self.state = self.initial_state.copy()
        self.bit_count = 0
    
    def get_state(self):
        """Get current state as string"""
        return ''.join(str(bit) for bit in self.state)

# Demonstration
print("=" * 60)
print("LFSR (LINEAR FEEDBACK SHIFT REGISTER) GENERATOR")
print("=" * 60)

# Example 1: 4-bit LFSR with taps at positions 0 and 3
print("\n--- Example 1: 4-bit LFSR ---")
print("Taps: positions 0 and 3 (feedback: state[0] XOR state[3])")

lfsr1 = LFSR(seed="1000", taps=[0, 3])
print(f"Initial state: {lfsr1.get_state()}")

# Generate 16 bits
bits = lfsr1.generate_sequence(16)
print(f"Generated bits: {bits}")
print(f"Bit sequence: {''.join(str(b) for b in bits)}")

# Reset and show more
lfsr1.reset()
print("\nFirst 20 bits (one by one):")
for i in range(20):
    bit = lfsr1.next_bit()
    print(f"Bit {i+1:2}: {bit} | State: {lfsr1.get_state()}")

# Example 2: Different configuration
print("\n" + "-" * 60)
print("\n--- Example 2: 5-bit LFSR ---")
print("Taps: positions 0 and 2 (different feedback polynomial)")

lfsr2 = LFSR(seed="11111", taps=[0, 2])
print(f"Initial state: {lfsr2.get_state()}")

# Generate 20 bits
bits2 = lfsr2.generate_sequence(20)
print(f"Generated sequence: {''.join(str(b) for b in bits2)}")

print("\n--- LFSR ANALYSIS ---")
print("✅ LFSR generates pseudorandom sequences")
print("✅ Used in stream ciphers like A5/1 (GSM encryption)")
print("⚠️ LFSR alone is NOT cryptographically secure")
print("⚠️ Can be predicted if polynomial and state are known")