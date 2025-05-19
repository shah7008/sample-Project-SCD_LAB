"""
Unit tests for the AuthService class.
"""

import unittest
from app.services.auth import AuthService


class TestAuthService(unittest.TestCase):
    """
    Test cases for the AuthService class.
    """

    def setUp(self):
        """Set up test fixtures."""
        self.auth_service = AuthService()

    def test_authenticate_valid_credentials(self):
        """Test authentication with valid credentials."""
        self.assertTrue(self.auth_service.authenticate("admin", "admin123"))
        self.assertTrue(self.auth_service.authenticate("user", "password123"))

    def test_authenticate_invalid_credentials(self):
        """Test authentication with invalid credentials."""
        self.assertFalse(self.auth_service.authenticate("admin", "wrongpass"))
        self.assertFalse(self.auth_service.authenticate("nonexistent", "password"))

    def test_authenticate_empty_credentials(self):
        """Test authentication with empty credentials."""
        self.assertFalse(self.auth_service.authenticate("", ""))
        self.assertFalse(self.auth_service.authenticate("admin", ""))
        self.assertFalse(self.auth_service.authenticate("", "admin123"))


if __name__ == "__main__":
    unittest.main()