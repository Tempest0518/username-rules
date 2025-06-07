print("\nUsername Rules:")
print("1. Must be between 3-20 characters.")
print("2. No spaces.")
print("3. No numbers.")
print("Please enter your username below: ")
username = input("\nInput Username: ")

while username:
    if len(username) < 3 or len(username) > 20:
        print("Error! Your username must be between 3 and 20 characters!")
        username = input("Enter your username: ")
    elif not username.find(" ") == -1:
        print("Error! Username can't have any spaces!")
        username = input("Enter your username: ")
    elif not username.isalpha():
        print("Error! Usernames can't have any numbers!")
        username = input("Enter your username: ")
    else:
        print(f"\nWelcome! {username}!")
        break
