# security/password_generator.py

import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generate a random password with specified constraints."""
    
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all character pools
    all_characters = lowercase + uppercase + numbers + symbols
    
    if len(all_characters) == 0:
        raise ValueError("At least one character type must be selected.")
    
    # Ensure the password contains at least one of each selected character type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(symbols))
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the resulting password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated Password:", generate_password(length=16, use_uppercase=True, use_numbers=True, use_symbols=True))