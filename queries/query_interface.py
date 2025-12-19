from auth.auth import authenticate
from access_control.roles import filter_fields

def demo_query(username: str, password: str):
    role = authenticate(username, password)
    if not role:
        print("Authentication failed")
        return

    # Example record (in your real project, this comes from MySQL)
    record = {
        "first_name": "Alice",
        "last_name": "Smith",
        "gender": "F",
        "age": 25,
        "weight": 65.0,
        "height": 165.0,
        "health_history": "No major illness"
    }

    print("Role:", role)
    print("Result:", filter_fields(role, record))

if __name__ == "__main__":
    demo_query("reader", "reader123")
