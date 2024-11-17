# database/models.py

class User:
    def __init__(self, user_id, username, email, password_hash):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"User (id={self.user_id}, username='{self.username}', email='{self.email}')"

class PasswordEntry:
    def __init__(self, entry_id, user_id, website, username, password):
        self.entry_id = entry_id
        self.user_id = user_id
        self.website = website
        self.username = username
        self.password = password

    def __repr__(self):
        return f"PasswordEntry(id={self.entry_id}, website='{self.website}', username='{self.username}')"