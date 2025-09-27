import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is a test email from Python.")
msg["Subject"] = "Hello"
msg["From"] = "mehedialam.pro@gmail.com"
msg["To"] = "mehedialam806@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("mehedialam.pro@gmail.com", "Mehedi#123")
    server.send_message(msg)
