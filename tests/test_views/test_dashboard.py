"""
Unit tests for the DashboardView class.
"""

import unittest
import tkinter as tk
from unittest.mock import MagicMock
from app.views.dashboard import DashboardView


class TestDashboardView(unittest.TestCase):
    """
    Test cases for the DashboardView class.
    """

    def setUp(self):
        """Set up test fixtures."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window during tests
        self.controller = MagicMock()
        self.dashboard_view = DashboardView(self.root, self.controller)

    def tearDown(self):
        """Clean up test fixtures."""
        self.root.destroy()

    def test_navigation_buttons(self):
        """Test that navigation buttons work correctly."""
        # Find all buttons
        buttons = [child for child in self.dashboard_view.children.values()
                   if isinstance(child, tk.Frame)][0].children.values()

        # Simulate button clicks
        for button in buttons:
            button.invoke()

        # Verify controller was called
        self.assertEqual(self.controller.show_view.call_count, 2)
        self.controller.show_view.assert_any_call("BillingView")
        self.controller.show_view.assert_any_call("LoginView")


if __name__ == "__main__":
    unittest.main()