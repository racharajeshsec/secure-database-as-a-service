from cryptography.fernet import Fernet

# For demo: generated each run. In real usage, load from secure config.
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_value(value) -> bytes:
    return cipher.encrypt(str(value).encode())

def decrypt_value(token: bytes) -> str:
    return cipher.decrypt(token).decode()
