"""
Dashboard view module.

This module contains the DashboardView class which provides the main application
dashboard after successful login.
"""

import tkinter as tk
from tkinter import ttk


class DashboardView(tk.Frame):
    """
    Dashboard view that shows after successful login.

    Attributes:
        controller (Application): The main application controller.
    """

    def __init__(self, parent, controller):
        """
        Initialize the dashboard view.

        Args:
            parent (tk.Widget): The parent widget.
            controller (Application): The main application controller.
        """
        super().__init__(parent)
        self.controller = controller

        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface elements for the dashboard view."""
        self.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(
            self,
            text="Dashboard",
            font=("Helvetica", 18, "bold"),
            bg="#f0f0f0"
        )
        header.pack(pady=(20, 30))

        # Navigation buttons
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        billing_btn = ttk.Button(
            btn_frame,
            text="Go to Billing",
            command=lambda: self.controller.show_view("BillingView")
        )
        billing_btn.pack(pady=10, fill=tk.X, padx=50)

        logout_btn = ttk.Button(
            btn_frame,
            text="Logout",
            command=lambda: self.controller.show_view("LoginView")
        )
        logout_btn.pack(pady=10, fill=tk.X, padx=50)

    def on_show(self):
        """Perform any necessary setup when the view is shown."""
        pass