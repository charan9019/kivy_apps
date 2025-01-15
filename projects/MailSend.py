import smtplib
from email.mime.text import MIMEText

text = MIMEText("Hii !")
text['Subject'] = 'Test Email!'
text['From'] = 'charancharudc99@gmail.com'
text['To'] = 'thepyking@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(text['From'], "trdr ukrx zfhy vibb")
server.send_message(text)
server.quit()

print('Sent  ! \nSuccesFully')