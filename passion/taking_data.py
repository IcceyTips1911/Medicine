import getpass
import sqlite3

# --- 1. DATABASE SETUP ---
# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("users_dashboard.db")
cursor = conn.cursor()

# Create a table for users
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
"""
)
conn.commit()


# --- 2. AUTHENTICATION FUNCTIONS ---
def register_user():
    """Takes user input and stores a new user in the database."""
    print("\n--- 📝 Create a New Account ---")
    username = input("Enter a new username: ").strip()
    # getpass hides the password typing in most terminals
    password = getpass.getpass("Enter a new password: ")

    if not username or not password:
        print("❌ Username and password cannot be empty.")
        return

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()
        print("✅ Registration successful! You can now log in.")
    except sqlite3.IntegrityError:
        print("❌ That username is already taken. Try another one.")


def login_user():
    """Verifies user credentials against the database."""
    print("\n--- 🔐 Log In ---")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    # Query database for the exact username and password match
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()

    if user:
        print(f"\n✅ Login successful! Welcome back, {username}.")
        run_dashboard(username)  # Send the user to the dashboard
    else:
        print("❌ Invalid username or password.")


# --- 3. DASHBOARD & FEATURES ---
def run_dashboard(username):
    """The main dashboard area after a successful login."""
    while True:
        print(f"\n=== 📊 DASHBOARD ({username}) ===")
        print("1. Mood Analysis")
        print("2. Run Analytics Tool")
        print("3. Log Out")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            print(f"\n👤 [Profile] Username: {username}")
            print("Status: Active User")
            from passion_2 import test_mental
            print(test_mental)
        elif choice == "2":
            from checker_call import syschecker
            syschecker()
        elif choice == "3":
            print(f"\n👋 Logged out successfully. Goodbye, {username}!")
            break  # Exits the dashboard loop, effectively logging the user out
        else:
            print("❌ Invalid choice. Please pick 1, 2, or 3.")


# --- 4. MAIN PROGRAM LOOP ---
def main():
    while True:
        print("\n=== 🔑 MAIN MENU ===")
        print("1. Register")
        print("2. Log In")
        print("3. Exit Program")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("\nClosing application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please pick 1, 2, or 3.")

    # Close connection when exiting the entire script
    conn.close()


if __name__ == "__main__":
    main()
