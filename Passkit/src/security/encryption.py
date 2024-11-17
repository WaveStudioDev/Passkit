# security/encryption.py

from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self):
        # Generate a key for encryption/decryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        """Encrypt the plaintext using the generated key."""
        if isinstance(plaintext, str):
            plaintext = plaintext.encode()  # Convert string to bytes
        encrypted = self.cipher.encrypt(plaintext)
        return encrypted

    def decrypt(self, encrypted_data):
        """Decrypt the encrypted data using the generated key."""
        decrypted = self.cipher.decrypt(encrypted_data)
        return decrypted.decode()  # Convert bytes back to string

    def save_key(self, file_path):
        """Save the encryption key to a file."""
        with open(file_path, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self, file_path):
        """Load the encryption key from a file."""
        with open(file_path, 'rb') as key_file:
            self.key = key_file.read()
            self.cipher = Fernet(self.key)

# Example usage
if __name__ == "__main__":
    encryption_manager = EncryptionManager()
    
    # Encrypting data
    original_data = "my_secret_password"
    encrypted_data = encryption_manager.encrypt(original_data)
    print(f"Encrypted: {encrypted_data}")

    # Decrypting data
    decrypted_data = encryption_manager.decrypt(encrypted_data)
    print(f"Decrypted: {decrypted_data}")

    # Save the key to a file
    encryption_manager.save_key("encryption_key.key")

    # Load the key from a file
    encryption_manager.load_key("encryption_key.key")