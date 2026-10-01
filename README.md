# 🔐 Secure Login & Authentication System

A Python-based secure login and authentication system that demonstrates password hashing, user registration, and login verification.

## 🚀 Features

- User registration
- Secure password hashing using PBKDF2-HMAC
- Password verification during login
- Unique salt generated for each password
- Protection against storing plain-text passwords
- Hidden password input using `getpass`
- Basic login attempt handling
- Local user data storage
- `.gitignore` protection for sensitive user data

## 🛠️ Technologies Used

- Python 3
- `hashlib`
- `secrets`
- `getpass`
- Git
- GitHub

## 📂 Project Structure

```text
secure-login-system/
│
├── login_system.py
├── .gitignore
└── README.md

🔒 Security

Passwords are never stored as plain text.

The system generates a unique random salt for each password and uses PBKDF2-HMAC with SHA-256 to derive a password hash.

The users.txt file is excluded from Git using .gitignore so local user data is not uploaded to GitHub.

▶️ How to Run

Clone the repository and open the project folder.

Run:

python login_system.py

Follow the prompts to register a user or log in.

📚 Learning Goals

This project demonstrates fundamental cybersecurity and backend concepts including:

Authentication
Password hashing
Salting
Secure credential handling
Input protection
File-based data storage
Git version control
⚠️ Disclaimer

This project is intended for educational purposes. A production authentication system should use a dedicated database, secure session management, rate limiting, and additional security controls.


Then press:

**Ctrl + S**

Don't commit it yet.

Tell me **“done”** once you've saved it.