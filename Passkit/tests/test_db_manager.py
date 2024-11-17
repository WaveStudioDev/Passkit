# tests/test_db_manager.py

import unittest
from database.db_manager import DBManager  # Adjust the import based on your actual DBManager implementation
from database.models import User  # Assuming you have a User model
import sqlite3

class TestDBManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a temporary database for testing."""
        cls.db_manager = DBManager(':memory:')  # Use an in-memory database for tests
        cls.db_manager.create_tables()  # Create tables for testing

    def test_create_user(self):
        """Test creating a user."""
        user = User(username='testuser', email='test@example.com')
        user_id = self.db_manager.create_user(user)
        self.assertIsNotNone(user_id)

    def test_read_user(self):
        """Test reading a user."""
        user = User(username='testuser2', email='test2@example.com')
        user_id = self.db_manager.create_user(user)
        retrieved_user = self.db_manager.get_user(user_id)
        self.assertEqual(retrieved_user.username, user.username)
        self.assertEqual(retrieved_user.email, user.email)

    def test_update_user(self):
        """Test updating a user."""
        user = User(username='testuser3', email='test3@example.com')
        user_id = self.db_manager.create_user(user)
        updated_user = User(username='updateduser', email='updated@example.com')
        self.db_manager.update_user(user_id, updated_user)
        retrieved_user = self.db_manager.get_user(user_id)
        self.assertEqual(retrieved_user.username, updated_user.username)
        self.assertEqual(retrieved_user.email, updated_user.email)

    def test_delete_user(self):
        """Test deleting a user."""
        user = User(username='testuser4', email='test4@example.com')
        user_id = self.db_manager.create_user(user)
        self.db_manager.delete_user(user_id)
        retrieved_user = self.db_manager.get_user(user_id)
        self.assertIsNone(retrieved_user)

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        cls.db_manager.close()

if __name__ == '__main__':
    unittest.main()