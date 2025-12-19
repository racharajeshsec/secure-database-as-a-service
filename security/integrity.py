import hmac
import hashlib

# Demo secret (do NOT hardcode in real deployments)
SECRET = b"demo-integrity-secret"

def make_tag(message: bytes) -> bytes:
    return hmac.new(SECRET, message, hashlib.sha256).digest()

def verify_tag(message: bytes, tag: bytes) -> bool:
    expected = make_tag(message)
    return hmac.compare_digest(expected, tag)
