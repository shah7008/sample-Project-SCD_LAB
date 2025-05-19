"""
Login view module.

This module contains the LoginView class which provides the GUI for user authentication
and handles the login process.
"""

import tkinter as tk
from tkinter import messagebox
from app.services.auth import AuthService


class LoginView(tk.Frame):
    """
    Login view that allows users to authenticate and access the application.

    Attributes:
        controller (Application): The main application controller.
        auth_service (AuthService): Service handling authentication logic.
    """

    def __init__(self, parent, controller):
        """
        Initialize the login view.

        Args:
            parent (tk.Widget): The parent widget.
            controller (Application): The main application controller.
        """
        super().__init__(parent)
        self.controller = controller
        self.auth_service = AuthService()

        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface elements for the login view."""
        # Style configuration
        self.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(
            self,
            text="Login to Application",
            font=("Helvetica", 18, "bold"),
            bg="#f0f0f0"
        )
        header.pack(pady=(50, 20))

        # Username field
        username_frame = tk.Frame(self, bg="#f0f0f0")
        username_frame.pack(pady=10)
        tk.Label(
            username_frame,
            text="Username:",
            bg="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)
        self.username_entry = tk.Entry(username_frame, width=25)
        self.username_entry.pack(side=tk.LEFT)

        # Password field
        password_frame = tk.Frame(self, bg="#f0f0f0")
        password_frame.pack(pady=10)
        tk.Label(
            password_frame,
            text="Password:",
            bg="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)
        self.password_entry = tk.Entry(password_frame, width=25, show="*")
        self.password_entry.pack(side=tk.LEFT)

        # Login button
        login_btn = tk.Button(
            self,
            text="Login",
            command=self._handle_login,
            width=15
        )
        login_btn.pack(pady=20)

        # Focus on username entry by default
        self.username_entry.focus_set()

    def _handle_login(self):
        """
        Handle the login button click event.

        Validates credentials and either shows an error message or
        transitions to the dashboard view on success.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        try:
            if self.auth_service.authenticate(username, password):
                self.controller.show_view("DashboardView")
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def on_show(self):
        """Reset the form when the view is shown."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus_set()