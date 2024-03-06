import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, message):
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Start SMTP server session
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)

        print("Email sent successfully to", receiver_email)

# Example usage:
        """
        sender = EmailSender('smtp.example.com', 587, 'your_email@example.com', 'your_password')

        receiver_email = 'recipient@example.com'
        subject = 'Test Email'
        message = 'This is a test email sent from Python.'

        sender.send_email(receiver_email, subject, message)
        """

