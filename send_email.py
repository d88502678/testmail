import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("EMAIL_RECEIVER")

subject = "📬 GitHub Action 測試信"
body = "你好，這是一封從 GitHub Action 自動寄出的測試信 🚀。"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("✅ 郵件發送成功！")
except Exception as e:
    print("❌ 發信失敗：", str(e))
