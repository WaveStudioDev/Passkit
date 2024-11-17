# tests/test_gui.py

import unittest
from unittest.mock import patch
import tkinter as tk
from gui.main_window import MainWindow  # Adjust the import based on your actual MainWindow implementation

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        """Set up the main window for testing."""
        self.root = tk.Tk()
        self.main_window = MainWindow(self.root)

    def tearDown(self):
        """Destroy the main window after tests."""
        self.root.destroy()

    def test_window_title(self):
        """Test that the window title is set correctly."""
        self.assertEqual(self.main_window.title(), "Your Application Title")  # Replace with your actual title

    def test_button_click(self):
        """Test that a button click performs the expected action."""
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.main_window.some_button.invoke()  # Replace with the actual button you want to test
            mock_showinfo.assert_called_once_with("Title", "Expected message")  # Replace with expected title and message

    def test_entry_field(self):
        """Test that the entry field accepts input."""
        self.main_window.entry_field.insert(0, "Test Input")  # Replace with your actual entry field
        self.assertEqual(self.main_window.entry_field.get(), "Test Input")

    def test_combobox_selection(self):
        """Test that the combobox selection works."""
        self.main_window.combobox.set("Option 1")  # Replace with your actual combobox
        self.assertEqual(self.main_window.combobox.get(), "Option 1")

if __name__ == '__main__':
    unittest.main()