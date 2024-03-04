import os
from fastapi import BackgroundTasks
from database import add_review_to_db
from models import Review
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_confirmation_email(book_id: int):
    sender_email = os.environ.get('email')
    recipient_email = os.environ.get('recipient_email')
    password = os.environ.get('password')
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Confirmation Email for Your Review"

    # Add body to email
    body = f"Thank you for submitting a review for book ID {book_id}."
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Confirmation email sent successfully!")
    except Exception as e:
        print(f"Failed to send confirmation email: {e}")
    finally:
        server.quit()  # Quit SMTP server connection


def add_review(review: Review, background_tasks: BackgroundTasks):
    add_review_to_db(review)
    background_tasks.add_task(send_confirmation_email, review.book_id)
    return {"message": "Review submitted successfully"}
