# Secure Database-as-a-Service (DBaaS)


---

## Overview
This project implements a **secure Database-as-a-Service (DBaaS)** system for storing and querying healthcare data in a **semi-trusted cloud environment**.

The system ensures that sensitive information remains confidential from the cloud provider while still supporting authorized queries.

---

## Threat Model
- The cloud/database server is **semi-trusted**
- The cloud follows the protocol but may attempt to infer sensitive data
- All cryptographic operations are performed client-side

---

##  System Architecture
- Client:
  - User authentication
  - Encryption / decryption
  - Query integrity & completeness verification
- Cloud Database:
  - Stores encrypted sensitive attributes
  - Executes SQL queries without access to plaintext data


---

##  Security Features

### User Authentication
- Custom username/password authentication
- Secure password hashing
- No plaintext password storage

### Role-Based Access Control
- **Group H:** Full read/write access
- **Group R:** Read-only access with restricted attributes
- Unauthorized fields are filtered before results are returned

### Data Confidentiality
- Sensitive attributes (`gender`, `age`) are encrypted before storage
- Encryption prevents both direct disclosure and statistical leakage

### Query Integrity Protection
- Cryptographic integrity tags allow detection of tampered or forged records

### Query Completeness Verification
- Detects missing records in query results with high probability

---

## 🛠️ Tech Stack
- Python
- MySQL
- Cryptography libraries
- Git / GitHub

---

## 📁 Repository Structure

secure-database-as-a-service/
├── auth/
├── access_control/
├── security/
├── queries/
├── database/
├── extra/
├── docs/
├── tests/
├── requirements.txt
└── README.md


---

## 🚀 How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Initialize database:
```
mysql < database/schema.sql
mysql < database/seed_data.sql
```

3. Run client:
```
python queries/query_interface.py
```
