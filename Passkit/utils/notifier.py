# utils/notifier.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

class Notifier:
    def __init__(self, email_config=None):
        """Initialize the notifier with optional email configuration."""
        self.email_config = email_config
        self.logger = logging.getLogger(__name__)

    def notify_console(self, message):
        """Send a notification to the console."""
        print(f"NOTIFICATION: {message}")
        self.logger.info(f"Console notification: {message}")

    def notify_email(self, subject, message):
        """Send an email notification."""
        if not self.email_config:
            raise ValueError("Email configuration not provided.")

        sender_email = self.email_config['sender_email']
        receiver_email = self.email_config['receiver_email']
        password = self.email_config['password']

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(sender_email, password)
                server.send_message(msg)
            self.logger.info(f"Email notification sent: {subject}")
        except Exception as e:
            self.logger.error(f"Failed to send email notification: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Configure email settings (for example purposes, replace with your actual credentials)
    email_config = {
        'sender_email': 'your_email@example.com',
        'receiver_email': 'recipient@example.com',
        'password': 'your_email_password',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587
    }

    notifier = Notifier(email_config)

    # Console notification
    notifier.notify_console("User  logged in successfully.")

    # Email notification
    try:
        notifier.notify_email("Login Notification", "User  logged in successfully.")
    except ValueError as e:
        print(e)