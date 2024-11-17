# tests/test_encryption.py

import unittest
from security.encryption import encrypt, decrypt  # Adjust the import based on your actual encryption implementation

class TestEncryptionMethods(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.secret_key = "my_secret_key"  # Replace with your actual secret key
        self.plain_text = "Hello, World!"

    def test_encryption(self):
        """Test the encryption method."""
        encrypted_text = encrypt(self.plain_text, self.secret_key)
        self.assertIsNotNone(encrypted_text)
        self.assertNotEqual(encrypted_text, self.plain_text)  # Ensure the encrypted text is not the same as plain text

    def test_decryption(self):
        """Test the decryption method."""
        encrypted_text = encrypt(self.plain_text, self.secret_key)
        decrypted_text = decrypt(encrypted_text, self.secret_key)
        self.assertEqual(decrypted_text, self.plain_text)  # Ensure the decrypted text matches the original plain text

    def test_decryption_invalid_key(self):
        """Test decryption with an invalid key."""
        encrypted_text = encrypt(self.plain_text, self.secret_key)
        with self.assertRaises(ValueError):
            decrypt(encrypted_text, "wrong_key")  # Attempt to decrypt with an incorrect key

if __name__ == '__main__':
    unittest.main()