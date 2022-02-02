import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Bob Smith'
email['to'] = 'developmentdiscords@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('developmentdiscords@gmail.com', '#C3a1R18r18I9e5+A1d4A1m13=113018!#')
	smtp.send_message(email)
	print('all good boss')