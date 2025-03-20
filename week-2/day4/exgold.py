import sqlite3
from tkinter import *
import hashlib
import os
 
def cli_version():
    users = {
        "kati": "pass123",
        "alice": "qwerty",
        "bob": "1369"
    }
    
    logged_in = None
    
    while True:
        action = input("Enter 'login', 'signup', or 'exit': ").lower()
        
        if action == "exit":
            print("Goodbye!")
            break
            
        elif action == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if username in users and users[username] == password:
                logged_in = username
                print("You are now logged in!")
            else:
                print("Invalid credentials")
                signup = input("Would you like to sign up? (yes/no): ").lower()
                if signup == "yes":
                    new_username = input("Enter new username: ")
                    while new_username in users:
                        print("Username already exists!")
                        new_username = input("Enter new username: ")
                    new_password = input("Enter new password: ")
                    users[new_username] = new_password
                    print("Signup successful!")
                    
        elif action == "signup":
            new_username = input("Enter new username: ")
            while new_username in users:
                print("Username already exists!")
                new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            users[new_username] = new_password
            print("Signup successful!")
 
class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication System")
      
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()
 
        self.label = Label(root, text="Authentication System")
        self.label.pack(pady=10)
        
        self.username_label = Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(root)
        self.username_entry.pack()
        
        self.password_label = Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(root, show="*")
        self.password_entry.pack()
        
        self.login_button = Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=5)
        
        self.signup_button = Button(root, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=5)
        
        self.status_label = Label(root, text="")
        self.status_label.pack(pady=10)
        
        self.logged_in = None

    def hash_password(self, password):
        salt = os.urandom(16)  # Generate random salt
        password_hash = hashlib.sha256(salt + password.encode()).hexdigest() # hash password
        return salt.hex() + password_hash

    def verify_password(self, stored_password, provided_password):
        salt = bytes.fromhex(stored_password[:32])  # First 32 chars are salt
        password_hash = stored_password[32:]
        new_hash = hashlib.sha256(salt + provided_password.encode()).hexdigest()
        return new_hash == password_hash

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        self.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        
        if result and self.verify_password(result[0], password):
            self.logged_in = username
            self.status_label.config(text=f"Logged in as {username}", fg="green")
        else:
            self.status_label.config(text="Invalid credentials or signup needed", fg="red")

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check username exists
        self.cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if self.cursor.fetchone():
            self.status_label.config(text="Username already exists!", fg="red")
            return
            
        # Store encrypted password
        encrypted_password = self.hash_password(password)
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                              (username, encrypted_password))
            self.conn.commit()
            self.status_label.config(text="Signup successful!", fg="green")
        except sqlite3.Error as e:
            self.status_label.config(text=f"Error: {e}", fg="red")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    app = AuthApp(root)
    root.mainloop()
