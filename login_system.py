import hashlib
import os
import getpass
import re

MAX_LOGIN_ATTEMPTS = 3

def hash_password(password, salt):
    password_bytes = password.encode("utf-8")
    hash_value = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt,
        100000
    )
    return hash_value

def verify_password(password, salt, stored_hash):
    new_hash = hash_password(password, salt)
    return new_hash == stored_hash

def valid_username(username):
    return re.fullmatch(r"[A-Za-z0-9_]{3,20}", username) is not None

def user_exists(username):
    try:
        with open("users.txt", "rb") as file:
            for line in file:
                parts = line.strip().split(b":")

                if len(parts) != 3:
                    continue

                stored_username = parts[0].decode("utf-8")

                if stored_username == username:
                    return True

        return False

    except FileNotFoundError:
        return False

def valid_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[^A-Za-z0-9]", password):
        return False

    return True

def register_user(username, password):
    if not valid_username(username):
        print("Invalid username. Use 3-20 letters, numbers, or underscores.")
        return

    if not valid_password(password):
        print("Password must be at least 8 characters and contain uppercase, lowercase, number, and special character.")
        return

    if user_exists(username):
        print("Username already exists.")
        return

    salt = os.urandom(16)
    password_hash = hash_password(password, salt)


    with open("users.txt", "ab") as file:
        file.write(username.encode("utf-8"))
        file.write(b":")
        file.write(salt.hex().encode("utf-8"))
        file.write(b":")
        file.write(password_hash.hex().encode("utf-8"))
        file.write(b"\n")

    print("User registered successfully.")

def login_user(username, password):
    try:
        with open("users.txt", "rb") as file:
            for line in file:
                parts = line.strip().split(b":")

                if len(parts) != 3:
                    continue

                stored_username = parts[0].decode("utf-8")
                salt = bytes.fromhex(parts[1].decode("utf-8"))
                stored_hash = bytes.fromhex(parts[2].decode("utf-8"))

                if stored_username == username:
                    if verify_password(password, salt, stored_hash):
                        print("Login successful.")
                        return True
                    else:
                        print("Incorrect password.")
                        return False

        print("User not found.")
        return False

    except FileNotFoundError:
        print("No users registered yet.")
        return False

def main():
    while True:
        print("\n=== Secure Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")

            for attempt in range(1, MAX_LOGIN_ATTEMPTS + 1):
                password = getpass.getpass("Enter password: ")

                if login_user(username, password):
                    break

                if attempt < MAX_LOGIN_ATTEMPTS:
                    print(f"Attempts remaining: {MAX_LOGIN_ATTEMPTS - attempt}")
                else:
                    print("Maximum login attempts reached.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()