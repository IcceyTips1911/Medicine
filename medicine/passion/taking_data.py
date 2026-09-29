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
            mood = int(input("How are you feeling today? Please rate your mood a scale from 1-10: "))
            print(f"Mood scale rating: {mood}")

            if 1 <= mood <= 5:
                print("What is wrong today?")
                print("Please choose a number to use: ")
                reason = int(input("1.Long Day \n2.Work was not all that \n3.Missing my lady \n4.Not motivated"))
                if reason == 1:
                    print("Would you like to have some soft sounds, regular music, podact, or Bible Sermon to help calm you down?")
                    ld_choice = int(input("1.Soft Sounds \n2.General Music \n3.Podcast \n4.Bible Sermon \nYour Answer: "))
                    if ld_choice == 1:
                        print("Is there a specific type of sound you would like for me to play sir?")
                        yon = input("Yes or No \nYour Answer: ")
                        if yon == "yes":
                            sounds = int(input("1.Rain \n2.White Noise \nYour Answer: "))
                            if sounds == 1:
                                print("Now playing Rain Sounds")
                            elif sounds == 2:
                                print("Now playing White Sounds")
                        else:
                            print("Now shuffling sounds.")
                    elif ld_choice == 2:
                        print("Please select the type of music:")
                        music = int(input("1.Country \n2.Gospel \n3.Rap \n4.R&B \n5.Old School \n6.Shuffle Play \nYour Answer: "))
                        if music == 1:
                            print("Now shuffling Country Music.")
                        elif music == 2:
                            print("Now shuffling Gospel Music.")
                        elif music == 3:
                            print("Now shuffling Rap Music.")
                        elif music == 4:
                            print("Now shuffling R&B Music.")
                        elif music == 5:
                            print("Now shuffling Old School Music.")
                        else:
                            print("Now shuffling music at random.")
                    elif ld_choice == 3:
                        print("Now playing tech podcast.")
                    elif ld_choice == 4:
                        print("Now playing Bible Sermon.")
                elif reason == 2:
                    print("Why was work not the best today?")
                elif reason == 3:
                    print("Would you Like for me to call Mrs. Johnson for you?")
                elif reason == 4:                                    
                    print("How would you like to handle the situation?")
            elif  6 <= mood <= 10:
                print("That's good.")
                print("Please choose something you would like for me to help you with:")
                topics = input("1.Sports \n2.Weather \nYour answer: ")
            else:
                print("Not valid")
        elif choice == "2":
            print("\n⚙️ [Analytics] Running calculations... System healthy!")
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
