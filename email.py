from dotenv import load_dotenv
import os
import smtplib

# Load environment variables
load_dotenv()

# Fetch email details
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
to_email = os.getenv("to_email")

# Debug prints
print(f"From Email: {from_email}")
print(f"Password Loaded: {'Yes' if password else 'No'}")
print(f"To Email: {to_email}")



