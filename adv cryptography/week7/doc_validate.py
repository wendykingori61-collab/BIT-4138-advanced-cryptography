"""
Secure Document Validation with Digital Signatures
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

def generate_keys():
    """Generate RSA key pair"""
    private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public = private.public_key()
    return private, public

def sign_document(document, private_key):
    """Sign a document using private key"""
    signature = private_key.sign(
        document.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

def verify_document(document, signature_b64, public_key):
    """Verify document signature using public key"""
    try:
        public_key.verify(
            base64.b64decode(signature_b64),
            document.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except:
        return False

print("=" * 60)
print("SECURE DOCUMENT VALIDATION SYSTEM")
print("=" * 60)

# Generate keys
private_key, public_key = generate_keys()
print("\n✅ RSA keys generated successfully")

# Documents to sign
documents = [
    "Employment Contract 2024 - Salary: $50,000 per year",
    "Non-Disclosure Agreement - Confidential Information",
    "Loan Approval Document - Amount: $10,000"
]

print("\n" + "=" * 60)
print("DOCUMENT SIGNING PROCESS")
print("=" * 60)

signed_docs = []
for doc in documents:
    signature = sign_document(doc, private_key)
    signed_docs.append((doc, signature))
    print(f"\nDocument: {doc[:50]}...")
    print(f"Signature: {signature[:40]}...")
    print("✅ SIGNED")

print("\n" + "=" * 60)
print("DOCUMENT VALIDATION RESULTS")
print("=" * 60)

for doc, sig in signed_docs:
    print(f"\nDocument: {doc[:50]}...")
    if verify_document(doc, sig, public_key):
        print("✅ VALID - Document is authentic")
    else:
        print("❌ INVALID - Document has been tampered")

print("\n" + "=" * 60)
print("TAMPERING DETECTION TEST")
print("=" * 60)

original = "Contract Value: $1000"
signature = sign_document(original, private_key)

print(f"Original document: {original}")
print(f"Signature: {signature[:40]}...")

# Verify original
if verify_document(original, signature, public_key):
    print("✅ Original: VALID")
else:
    print("❌ Original: INVALID")

# Tamper with document
tampered = "Contract Value: $10000"
print(f"\nTampered document: {tampered}")

if verify_document(tampered, signature, public_key):
    print("❌ TAMPERED: Would be VALID (BAD - detection failed!)")
else:
    print("✅ TAMPERED: INVALID - Tampering successfully detected!")

print("\n" + "=" * 60)
print("REAL-WORLD APPLICATIONS")
print("=" * 60)
print("✅ Software updates (Microsoft, Apple)")
print("✅ Email security (DKIM signatures)")
print("✅ Legal documents (DocuSign)")
print("✅ Blockchain transactions")
print("✅ Code signing certificates")