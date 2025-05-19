"""
Unit tests for the LoginView class.
"""

import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from app.views.login import LoginView


class TestLoginView(unittest.TestCase):
    """
    Test cases for the LoginView class.
    """

    def setUp(self):
        """Set up test fixtures."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window during tests
        self.controller = MagicMock()
        self.login_view = LoginView(self.root, self.controller)

    def tearDown(self):
        """Clean up test fixtures."""
        self.root.destroy()

    def test_initial_state(self):
        """Test the initial state of the login view."""
        self.assertEqual(self.login_view.username_entry.get(), "")
        self.assertEqual(self.login_view.password_entry.get(), "")

    @patch("app.views.login.messagebox")
    @patch.object(LoginView, "_handle_login")
    def test_login_button_click(self, mock_handle_login, mock_messagebox):
        """Test that login button click calls the handler."""
        # Simulate button click
        self.login_view.children["!button"].invoke()
        mock_handle_login.assert_called_once()

    @patch("app.views.login.messagebox")
    @patch("app.services.auth.AuthService.authenticate")
    def test_handle_login_success(self, mock_authenticate, mock_messagebox):
        """Test successful login handling."""
        # Setup mocks
        mock_authenticate.return_value = True

        # Set test values
        self.login_view.username_entry.insert(0, "admin")
        self.login_view.password_entry.insert(0, "admin123")

        # Call the method
        self.login_view._handle_login()

        # Verify results
        mock_authenticate.assert_called_once_with("admin", "admin123")
        self.controller.show_view.assert_called_once_with("DashboardView")
        mock_messagebox.showerror.assert_not_called()

    @patch("app.views.login.messagebox")
    @patch("app.services.auth.AuthService.authenticate")
    def test_handle_login_failure(self, mock_authenticate, mock_messagebox):
        """Test failed login handling."""
        # Setup mocks
        mock_authenticate.return_value = False

        # Set test values
        self.login_view.username_entry.insert(0, "admin")
        self.login_view.password_entry.insert(0, "wrongpass")

        # Call the method
        self.login_view._handle_login()

        # Verify results
        mock_authenticate.assert_called_once_with("admin", "wrongpass")
        self.controller.show_view.assert_not_called()
        mock_messagebox.showerror.assert_called_once_with("Error", "Invalid username or password")


if __name__ == "__main__":
    unittest.main()