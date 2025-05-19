"""
Style utilities module.

This module contains functions for configuring the application's visual style.
"""

import tkinter as tk
from tkinter import ttk


def configure_styles():
    """Configure the global styles for the application."""
    style = ttk.Style()

    # Configure the default theme
    style.theme_use("clam")

    # Configure button styles
    style.configure(
        "TButton",
        padding=6,
        relief="flat",
        background="#4a6baf",
        foreground="white"
    )
    style.map(
        "TButton",
        background=[("active", "#3a5a9f")],
        relief=[("pressed", "sunken"), ("!pressed", "flat")]
    )

    # Configure entry styles
    style.configure(
        "TEntry",
        padding=5,
        relief="flat",
        fieldbackground="white"
    )

    # Configure treeview styles
    style.configure(
        "Treeview",
        background="white",
        fieldbackground="white",
        rowheight=25
    )
    style.configure(
        "Treeview.Heading",
        background="#4a6baf",
        foreground="white",
        padding=5,
        relief="flat"
    )
    style.map(
        "Treeview.Heading",
        relief=[("pressed", "sunken"), ("!pressed", "flat")]
    )