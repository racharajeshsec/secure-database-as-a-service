
---  
## 1. System Architecture  
The system architecture shows how a user interacts with a secure web-based application for managing healthcare data. You can sign-up, sign-in, see patients’ data, add new data (if allowed), and then log out, all securely. The web app communicates with the database server to authenticate users and retrieve or store records. Sensitive security functions including authentication, encryption, and access control are run at the application level, not in the cloud database.  

---  
## 2. The Main Components and Their Importance  
The Secure Database-as-a-Service (DBaaS) architecture comprises the following elements:  

### User Interface  
The User Interface shows a web app which users utilize. It permits authorized users to access or manage patient information per their assigned roles.  

### Web Server  
The web server facilitates users’ requests, handles authentication and authorization and securely communicates with the database. It is the intermediate trusted connection between the users and the cloud database.  

### Database-as-a-Service (DBaaS)  
The DBaaS stores medical records. Sensitive attributes are encrypted prior to storage in the database and are not accessible to the cloud provider in plaintext.  

### Authentication and Access Control Module  
This module verifies user credentials and enforces role-based access control. Only authenticated users are permitted access to the system; permissions are granted according to user roles.  

### Database  
The database records medical records, comprising encrypted sensitive information such as age and gender. Records availability is strictly controlled by the application.  

---  
## 3. Security Features Implementation  

### User Authentication  
**Implementation:**  
The system utilizes a username and password-based authentication mechanism. Passwords are encrypted using Fernet and securely held on the application server rather than stored on the cloud database.  
**Reason:**  
This protects credentials by preventing plaintext password storage and ensures security even if stored data is breached.  

---  
### Basic Access Control Mechanism  
**Implementation:**  
RBAC is developed with two user roles namely:  
- **Group H:** full patient attributes access, and the access to add new records.  
- **Group R:** read-only access with restricted visibility of first and last names.  
Application-level filtering is done for the query results before being returned to the user.  
**Reason:**  
This restricts access to data only to what users are authorized to access and prevents unauthorized data exposure.  

---  
### Basic Query Integrity Protection  
**Implementation:**  
Each database record includes a cryptographic hash generated using SHA-256. The hash is recomputed and verified before showing query results.  
**Reason:**  
This guarantees data integrity and enables detection of unauthorized data modification.  

---  
### Single Data Item Integrity  
**Implementation:**  
Integrity checks are applied to individual patient records using cryptographic hashing.  
**Reason:**  
Any modification to a record can be detected, confirming authenticity and trustworthiness of the returned data.  

---  
### Query Completeness  
**Implementation:**  
The system verifies the completeness of query results using consistency and probabilistic verification methods.  
**Reason:**  
This protects against intentional omission of records by the cloud database.  

---  
### Basic Data Confidentiality Protection  
**Implementation:**  
Sensitive attributes such as age and gender are encrypted prior to storage and decrypted only for authorized users at the application layer.  
**Reason:**  
This prevents unauthorized access to private healthcare data and avoids statistical data leakage.  

---  
## 4. Author Contributions  
This was implemented as an individual project.  

**Rajesh Racha** worked on:  
- System architecture design  
- Defining authentication and access control  
- Establishing encryption and confidentiality protocols  
- Ensuring query integrity and completeness validation  
- Database integration  
- Writing the project report  
- Maintaining the GitHub repository  

**GitHub Profile:**  
https://github.com/rajeshrachasec  

---  
## 5. Limitations of the Project  
- Users with direct database access may bypass application-level integrity checks.  
- Encryption keys are stored within the application code.  
- No audit logging or rollback mechanism is implemented.  
- Authorization is limited to two roles without finer-grained permissions.  
- The system does not implement multi-factor authentication (MFA).  
- Data masking is not implemented for development or testing environments.  

---  
## Conclusion  
This work presents the design and development of a secure Database-as-a-Service system to protect sensitive healthcare-related data in a semi-trusted cloud environment. The system, based on authentication, access control, encryption, and integrity verification, provides strong foundational security while maintaining usability.
