import smtplib
from password import passw
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email):
    # Configuración del servidor SMTP de Gmail y las credenciales de tu cuenta
    smtp_server = 'smtp.outlook.com'
    smtp_port = 587
    smtp_username = 'nomorephishing@hotmail.com'
    smtp_password = passw

    # Crear el objeto del mensaje
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = email
    message['Subject'] = 'Be careful! Stolen Credentials'

    # Agregar el cuerpo del correo

    message.attach(MIMEText('Dear reader \n \nYou logged in an insecure website or app where you use this email and your password has been exposed. We deleted your password from the message sent to the attacker, but please consider changing it in case it has been compromised. \nWe were able to intercept the attack using the tool Telegram-Hitbackscammer. For more information refer to ', 'plain'))
    message.attach(MIMEText(u'<a href="https://github.com/avechuch0/telegram-hitbackscammer">Telegram-HitbackScammer.</a>','html'))
    message.attach(MIMEText('If you have any questions, you can write to us using this email.\n \n', 'plain'))
    message.attach(MIMEText('Att: NoMorePhishingUR', 'plain'))
    

    # Iniciar la conexión con el servidor SMTP de Outlook
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(smtp_username, smtp_password)  
        try:
            server.send_message(message)  # Send message
            print('Alert message was sent :D')
        except: 
            print('Alert message was not sent D:')

