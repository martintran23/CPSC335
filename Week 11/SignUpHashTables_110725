def username_checker():
    used = set()
    
    print("Enter usernames to register. Type 'Exit' to stop.")
    while True:
        username = input("Username: ").strip()
        
        if username.lower() == "exit":
            print("Stopping the Registration.")
            break
        if username in used:
            print("🚫 Username is already taken. Choose another.")
        else:
            used.add(username)
            print("✅ Username registered successfully.")
            
    print("\nRegistered usernames:", used)
    
if __name__ == "__main__":
    username_checker()
    