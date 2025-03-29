import hashlib
import json
import os

CREDENTIALS_FILE = "creds.json"

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def new_user():
    username = input("Create Username: ")
    credentials = load_credentials()

    if username in credentials:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Create Password: ")
    credentials[username] = hash_password(password)
    save_credentials(credentials)
    print("User created successfully")

def sign_in():
    username = input("Username: ")
    password = input("Password: ")
    credentials = load_credentials()
    if credentials.get(username) == hash_password(password):
        print("You are now logged in")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input("1. New user\n2. Login\nType any other key to exit\n>>> ")
        if choice == '1':
            new_user()
        elif choice == '2':
            sign_in()
        else:
            break

if __name__ == "__main__":
    main()

# i need a file called cred.json for this program to work. Example of dictionary
# {"charlie": "b9dd960c1753459a78115d3cb845a57d924b6877e805b08bd01086ccdf34433c"}