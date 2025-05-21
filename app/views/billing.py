"""
Billing view module.

This module contains the BillingView class which provides the interface for
billing and invoice management.
"""

import tkinter as tk
from tkinter import ttk


class BillingView(tk.Frame):
    """
    Billing view for managing invoices and billing information.

    Attributes:
        controller (Application): The main application controller.
    """

    def __init__(self, parent, controller):
        """
        Initialize the billing view.

        Args:
            parent (tk.Widget): The parent widget.
            controller (Application): The main application controller.
        """
        super().__init__(parent)
        self.controller = controller

        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface elements for the billing view."""
        self.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(
            self,
            text="Billing Management",
            font=("Helvetica", 18, "bold"),
            bg="#f0f0f0"
        )
        header.pack(pady=(20, 30))

        # Billing form
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(pady=10, padx=20, fill=tk.X)

        # Customer name
        tk.Label(
            form_frame,
            text="Customer Name:",
            bg="#f0f0f0"
        ).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.customer_name = tk.Entry(form_frame, width=30)
        self.customer_name.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Items table
        columns = ("item", "quantity", "price", "total")
        self.items_table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=5
        )

        # Configure columns
        self.items_table.heading("item", text="Item")
        self.items_table.heading("quantity", text="Quantity")
        self.items_table.heading("price", text="Price")
        self.items_table.heading("total", text="Total")

        self.items_table.column("item", width=150)
        self.items_table.column("quantity", width=80, anchor=tk.CENTER)
        self.items_table.column("price", width=80, anchor=tk.E)
        self.items_table.column("total", width=80, anchor=tk.E)

        self.items_table.pack(pady=20, padx=20, fill=tk.X)

        # Add sample data
        self._add_sample_data()

        # Buttons
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        generate_btn = ttk.Button(
            btn_frame,
            text="Generate Invoice",
            command=self._generate_invoice
        )
        generate_btn.pack(side=tk.LEFT, padx=10)

        back_btn = ttk.Button(
            btn_frame,
            text="Back to Dashboard",
            command=lambda: self.controller.show_view("DashboardView")
        )
        back_btn.pack(side=tk.LEFT, padx=10)

    def _add_sample_data(self):
        """Add sample data to the items table."""
        sample_items = [
            ("Product A", 2, 25.00, 50.00),
            ("Product B", 1, 45.50, 45.50),
            ("Service C", 1, 75.00, 75.00)
        ]

        for item in sample_items:
            self.items_table.insert("", tk.END, values=item)

    def _generate_invoice(self):
        """Handle invoice generation."""
        customer = self.customer_name.get()
        if not customer:
            tk.messagebox.showerror("Error", "Please enter customer name")
            return

        # In a real app, this would generate and save an invoice
        tk.messagebox.showinfo(
            "Success",
            f"Invoice generated for {customer}\nTotal: $170.50"
        )

    def on_show(self):
        """Perform any necessary setup when the view is shown."""
        self.customer_name.delete(0, tk.END)