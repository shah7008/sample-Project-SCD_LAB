Project directory structure
tkinter_app/
│── app/                  # Main application package
│   │── __init__.py       # Package initialization
│   │── main.py           # Application entry point
│   │── views/            # GUI views/windows
│   │   │── login.py      # Login window
│   │   │── dashboard.py  # Dashboard window
│   │   │── billing.py    # Billing window
│   │── models/           # Data models
│   │   │── user.py       # User model
│   │── services/         # Business logic
│   │   │── auth.py       # Authentication service
│   │── utils/            # Utility functions
│   │   │── style.py      # Styling utilities
│── tests/                # Unit tests
│   │── test_views/
│   │   │── test_login.py
│   │   │── test_dashboard.py
│   │   │── test_billing.py
│   │── test_services/
│   │   │── test_auth.py
│── requirements.txt      # Project dependencies
