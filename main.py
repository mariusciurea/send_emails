import send_email as mail

mail_sender = input('e-mail from: ')
mail_receiver = input('e-mail to: ')
subject = input('e-mail subject: ')
body = input('e-mail body: ')

# Create an instance of EmailMessage()
msg = mail.EmailMessage()
msg['From'] = mail_sender
msg['To'] = mail_receiver
msg['Subject'] = subject
msg.set_content(body)

# Get the password from config.ini file
password = mail.get_config_data()

# send the e-mail
mail.send_mail(msg, mail_sender, mail_receiver, password)
