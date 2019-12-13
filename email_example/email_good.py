import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Armand'
email['to'] = 'jjbond621@gmail.com'
email['subject'] = 'You got Big Bonus'

email.set_content(html.substitute({'name': 'Teddy'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('armandsimbolon21@gmail.com', 'ArmandMartubung2019')
    smtp.send_message(email)
    print('all good boss!')
    