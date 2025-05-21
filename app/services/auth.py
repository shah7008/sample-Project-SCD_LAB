"""
Authentication service module.

This module contains the AuthService class which handles user authentication logic.
"""


class AuthService:
    """
    Service for handling user authentication.

    In a real application, this would interface with a database or external auth service.
    For this example, we're using hardcoded credentials.
    """

    def __init__(self):
        """Initialize the authentication service."""
        # In a real app, these would come from a database
        self.valid_users = {
            "admin": "admin123",
            "user": "password123"
        }

    def authenticate(self, username, password):
        """
        Authenticate a user with the provided credentials.

        Args:
            username (str): The username to authenticate.
            password (str): The password to verify.

        Returns:
            bool: True if authentication succeeds, False otherwise.
        """

        return self.valid_users.get(username) == password