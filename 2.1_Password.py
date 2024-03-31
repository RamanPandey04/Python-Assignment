def validate_password(password, username, last_three_passwords):
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."

    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if char in "!@#$%^&*")
    
    if uppercase_count < 2 or lowercase_count < 2 or digit_count < 2 or special_count < 2:
        return False, "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters."

    for i in range(len(username) - 2):
        if username[i:i+3] in password:
            return False, "Password cannot contain sequences of three or more consecutive characters from the username."

    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return False, "No character should repeat more than three times in a row."

    if password in last_three_passwords:
        return False, "Password cannot be the same as any of the last three passwords."

    return True, "Password is valid."

def main():
    username = input("Enter your username: ")
    last_three_passwords = []

    while True:
        password = input("Enter your new password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password set successfully!")
            break
        else:
            print("Password validation failed:", message)

main()