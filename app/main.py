"""
Main entry point for the Tkinter GUI application.

This module initializes the application, sets up the main window,
and manages the navigation between different views (login, dashboard, billing).
"""

import tkinter as tk
from app.views.login import LoginView
from app.utils.style import configure_styles


class Application(tk.Tk):
    """
    Main application class that inherits from tk.Tk.
    Manages the application lifecycle and view transitions.
    """

    def __init__(self):
        """Initialize the application with default settings."""
        super().__init__()

        self.title("Tkinter GUI Application")
        self.geometry("800x600")
        self.resizable(True, True)

        # Configure application styles
        configure_styles()

        # Container for all views
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold all views
        self.views = {}

        # Initialize all views
        self._initialize_views()

        # Show the login view first
        self.show_view("LoginView")

    def _initialize_views(self):
        """Initialize and register all application views."""
        from app.views.dashboard import DashboardView
        from app.views.billing import BillingView

        # Create instances of all views
        for ViewClass in (LoginView, DashboardView, BillingView):
            view_name = ViewClass.__name__
            view = ViewClass(self.container, self)
            self.views[view_name] = view
            view.grid(row=0, column=0, sticky="nsew")

    def show_view(self, view_name):
        """Bring the specified view to the front.

        Args:
            view_name (str): The name of the view class to show.
        """
        view = self.views[view_name]
        view.tkraise()
        view.on_show()  # Call view's on_show method for any setup


def main():
    """Entry point for the application."""
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()