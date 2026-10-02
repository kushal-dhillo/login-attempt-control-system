# Login Attempt Control System

correct_password = "Cyber123"
max_attempts = 3
attempts = 0

print("=== Login Attempt Control System ===")

while attempts < max_attempts:

    password = input("Enter your password: ")

    if password == correct_password:
        print("\nLogin successful!")
        print("Access granted.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts

        print("\nIncorrect password!")

        if remaining > 0:
            print("Attempts remaining:", remaining)

if attempts == max_attempts:
    print("\nToo many failed attempts!")
    print("Access temporarily restricted.")
