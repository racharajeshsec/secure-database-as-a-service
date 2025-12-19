# Secure Database-as-a-Service (DBaaS)

## 📌 Overview
This project provides for the design, implementation and evaluation of a **secure database-as-a-service (DBaaS)** solution for storing and querying healthcare data in a **semi-trusted cloud environment**. The system safeguards against a curious or malicious cloud provider but allows authorized users to make useful queries.

---

##  Threat Model
- The cloud/database server is **semi-trusted**  
- The cloud obeys protocol but may try and infer sensitive information  
- Users are authenticated clients  
- All sensitive fields must remain confidential from the cloud  

---

##  System Architecture
- Client-side application handles:  
  - Authentication  
  - Encryption / decryption  
  - Integrity & completeness verification  
- Cloud-side database stores:  
  - Encrypted sensitive fields  
  - Integrity metadata  
  - Non-sensitive attributes in plaintext  


---

##  Security Features Implemented

### 1. User Authentication
- Username/password-based authentication  
- Passwords are **hashed** (no plaintext storage)  
- Custom authentication logic (not DB-native auth)  

### 2. Role-Based Access Control
- **Group H:** Full access (read + insert)  
- **Group R:** Read-only, restricted attributes  
- First name & last name hidden from Group R  

### 3. Data Confidentiality
- Sensitive fields:  
  - `gender`  
  - `age`  
- Encrypted before storage using symmetric encryption  
- Cloud never sees plaintext values  
- Encryption prevents statistical leakage  

### 4. Query Integrity Protection
- Each data record includes a cryptographic integrity tag  
- Clients verify returned records to detect tampering or forgery  
- Works for both Group H and Group R users  

### 5. Query Completeness Verification
- Detects missing records in query results  
- Uses probabilistic verification techniques  

---

##  Extra Credit: Order Preserving Encryption (OPE)
- Applied Order Preserving Encryption to `weight`  
- Enables secure range queries (e.g., 60kg–80kg)  
- Preserves order without revealing exact values  


---

## 🛠️ Technology Stack
- **Language:** Python  
- **Database:** MySQL  
- **Crypto:** Python Cryptography libraries  
- **Version Control:** Git / GitHub  

---
