# tests/test_utils.py

import unittest
from utils.validators import validate_email, validate_password  # Adjust the import based on your actual validators implementation
from utils.validators import password_strength  # Adjust the import based on your actual password_strength implementation
class TestValidators(unittest.TestCase):
    def test_validate_email(self):
        """Test the validate_email function."""
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("test example.com"))
        self.assertFalse(validate_email("test@com"))

    def test_validate_password(self):
        """Test the validate_password function."""
        self.assertTrue(validate_password("SecureP@ssw0rd123"))
        self.assertFalse(validate_password("password"))
        self.assertFalse(validate_password("12345678"))
        self.assertFalse(validate_password(""))

class TestPasswordStrength(unittest.TestCase):
    def test_password_strength(self):
        """Test the password_strength function."""
        self.assertEqual(password_strength("SecureP@ssw0rd123"), "strong")
        self.assertEqual(password_strength("SecureP@ssw0rd"), "medium")
        self.assertEqual(password_strength("password"), "weak")
        self.assertEqual(password_strength("12345678"), "very_weak")
        self.assertEqual(password_strength(""), "none")
if __name__ == '__main__':
    unittest.main()