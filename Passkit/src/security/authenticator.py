# security/authenticator.py

import bcrypt
from database.models import User  # Assuming User model is defined in models.py
from database.db_manager import get_session  # Function to get a database session

class Authenticator:
    def __init__(self, db_manager):
        self.db_manager = db_manager  # Store the db_manager
        self.session = get_session(self.db_manager.db_file)  # Pass the db_file to get_session

    def register_user(self, username, email, password):
        """Register a new user with a hashed password."""
        # Check if the user already exists
        if self.session.query(User).filter_by(username=username).first() is not None:
            raise ValueError("Username already exists.")
        
        if self.session.query(User).filter_by(email=email).first() is not None:
            raise ValueError("Email already exists.")

        # Hash the password
        hashed_password = self.hash_password(password)

        # Create a new user instance
        new_user = User(username=username, email=email, password_hash=hashed_password)

        # Add the user to the session and commit
        self.session.add(new_user)
        self.session.commit()
        print(f"User  {username} registered successfully.")

    def login_user(self, username, password):
        """Authenticate a user with username and password."""
        user = self.session.query(User).filter_by(username=username).first()
        
        if user is None:
            raise ValueError("User  not found.")
        
        if not self.check_password(password, user.password_hash):
            raise ValueError("Invalid password.")
        
        print(f"User  {username} logged in successfully.")
        return user

    def hash_password(self, password):
        """Hash a password using bcrypt."""
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def check_password(self, password, hashed):
        """Check if the provided password matches the hashed password."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example usage
if __name__ == "__main__":
    # You need to create a DatabaseManager instance and pass it to Authenticator
    from database.db_manager import DatabaseManager

    db_file = "path_to_your_database.db"  # Update this path to your actual database file
    db_manager = DatabaseManager(db_file)
    
    auth = Authenticator(db_manager)
    
    # Register a new user
    try:
        auth.register_user(username="testuser", email="test@example.com", password="securepassword123")
    except ValueError as e:
        print(e)

    # Login with the user
    try:
        user = auth.login_user(username="testuser", password="securepassword123")
        print(f"Logged in as: {user.username}")
    except ValueError as e:
        print(e)