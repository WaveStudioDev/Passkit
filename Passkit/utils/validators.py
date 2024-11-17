# utils/validators.py

import re

def validate_username(username):
    """Validate the username."""
    if len(username) < 3 or len(username) > 20:
        raise ValueError("Username must be between 3 and 20 characters long.")
    if not re.match("^[a-zA-Z0-9_]+$", username):
        raise ValueError("Username can only contain letters, numbers, and underscores.")
    return True

def validate_password(password):
    """Validate the password."""
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not re.search("[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search("[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search("[0-9]", password):
        raise ValueError("Password must contain at least one digit.")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError("Password must contain at least one special character.")
    return True

def validate_email(email):
    """Validate the email address."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email address format.")
    return True

def validate_phone_number(phone_number):
    """Validate the phone number."""
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
    if not re.match(phone_regex, phone_number):
        raise ValueError("Invalid phone number format. Use E.164 format.")
    return True

# Example usage
if __name__ == "__main__":
    try:
        validate_username("test_user")
        print("Username is valid.")
    except ValueError as e:
        print(e)

    try:
        validate_password("Password123!")
        print("Password is valid.")
    except ValueError as e:
        print(e)

    try:
        validate_email("test@example.com")
        print("Email is valid.")
    except ValueError as e:
        print(e)

    try:
        validate_phone_number("+1234567890")
        print("Phone number is valid.")
    except ValueError as e:
        print(e)