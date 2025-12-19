import hashlib

# Demo users (replace with DB-backed users if your project uses that)
USERS = {
    "admin": {
        "password_hash": hashlib.sha256("admin123".encode()).hexdigest(),
        "role": "H"
    },
    "reader": {
        "password_hash": hashlib.sha256("reader123".encode()).hexdigest(),
        "role": "R"
    }
}

def authenticate(username: str, password: str):
    user = USERS.get(username)
    if not user:
        return None
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash == user["password_hash"]:
        return user["role"]
    return None
