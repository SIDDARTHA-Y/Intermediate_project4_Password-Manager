import json

PASSWORD_FILE = "passwords.json"

def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def add_password(site, username, password):
    passwords = load_passwords()
    passwords[site] = {"username": username, "password": password}
    save_passwords(passwords)
    print("Password saved!")

if __name__ == "__main__":
    site = input("Enter site: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_password(site, username, password)
