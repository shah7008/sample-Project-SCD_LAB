"""
Unit tests for the BillingView class.
"""

import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch
from app.views.billing import BillingView


class TestBillingView(unittest.TestCase):
    """
    Test cases for the BillingView class.
    """

    def setUp(self):
        """Set up test fixtures."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window during tests
        self.controller = MagicMock()
        self.billing_view = BillingView(self.root, self.controller)

    def tearDown(self):
        """Clean up test fixtures."""
        self.root.destroy()

    def test_initial_state(self):
        """Test the initial state of the billing view."""
        self.assertEqual(self.billing_view.customer_name.get(), "")
        self.assertGreater(len(self.billing_view.items_table.get_children()), 0)

    @patch("tkinter.messagebox")
    def test_generate_invoice_empty_customer(self, mock_messagebox):
        """Test invoice generation with empty customer name."""
        # Ensure customer name is empty
        self.billing_view.customer_name.delete(0, tk.END)

        # Call the method
        self.billing_view._generate_invoice()

        # Verify error message was shown
        mock_messagebox.showerror.assert_called_once_with("Error", "Please enter customer name")

    @patch("tkinter.messagebox")
    def test_generate_invoice_valid(self, mock_messagebox):
        """Test successful invoice generation."""
        # Set customer name
        self.billing_view.customer_name.insert(0, "Test Customer")

        # Call the method
        self.billing_view._generate_invoice()

        # Verify success message was shown
        mock_messagebox.showinfo.assert_called_once_with(
            "Success",
            "Invoice generated for Test Customer\nTotal: $170.50"
        )

    def test_navigation_buttons(self):
        """Test that navigation buttons work correctly."""
        # Find all buttons
        buttons = [child for child in self.billing_view.children.values()
                   if isinstance(child, tk.Frame)][-1].children.values()

        # Simulate button clicks
        for button in buttons:
            button.invoke()

        # Verify controller was called
        self.assertEqual(self.controller.show_view.call_count, 2)
        self.controller.show_view.assert_any_call("DashboardView")


if __name__ == "__main__":
    unittest.main()