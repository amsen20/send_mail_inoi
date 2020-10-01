# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content("سلام کیوان")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = ':))'
msg['From'] = "ahph1380@gmail.com"
msg['To'] = "ahph1380@gmail.com"

# Send the message via our own SMTP server.
print(msg)
s = smtplib.SMTP('localhost')
print(s)
s.send_message(msg)
s.quit()
