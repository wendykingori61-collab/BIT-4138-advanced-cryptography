from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(message, private_key):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

def verify_signature(message, signature_b64, public_key):
    signature = base64.b64decode(signature_b64)
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

print("=" * 60)
print("DIGITAL SIGNATURE DEMONSTRATION")
print("=" * 60)

print("\n--- Generating RSA Key Pair ---")
private_key, public_key = generate_key_pair()
print("✅ RSA key pair generated")

document = "This is an important contract. I agree to the terms."
print(f"\nDocument: {document}")

print("\n--- SIGNING THE DOCUMENT ---")
signature = sign_message(document, private_key)
print(f"Digital Signature: {signature[:60]}...")
print("✅ Document signed with PRIVATE key")

print("\n--- VERIFYING THE SIGNATURE ---")
is_valid = verify_signature(document, signature, public_key)
if is_valid:
    print("✅ SIGNATURE VALID! Document is authentic.")
else:
    print("❌ SIGNATURE INVALID!")

print("\n--- TESTING TAMPERED DOCUMENT ---")
tampered = document + " (hacked)"
is_valid = verify_signature(tampered, signature, public_key)
if is_valid:
    print("✅ SIGNATURE VALID!")
else:
    print("❌ SIGNATURE INVALID! Tampering detected.")

print("\n" + "=" * 60)
print("✅ Digital Signatures provide:")
print("   - Authentication (proves who signed it)")
print("   - Integrity (proves no tampering)")
print("   - Non-repudiation (cannot deny signing)")