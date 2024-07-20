import smtplib
from email.message import EmailMessage
from config import smtp_user, smtp_password

def send_email(to_email, subject, message, image_path=None):
    sender = smtp_user
    password = smtp_password
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(sender, password)
        
        msg = EmailMessage()
        msg['Subject'] = subject  # Не нужно явно кодировать тему, если она уже в формате Unicode
        msg['From'] = sender
        msg['To'] = to_email
        msg.set_content(message, subtype='plain', charset='utf-8')  # Кодируем содержимое сообщения как UTF-8
        
        if image_path:
            with open(image_path, 'rb') as img:
                img_data = img.read()
                msg.add_attachment(img_data, maintype='image', subtype='jpg', filename=image_path)
        
        server.send_message(msg)
        return '200 OK'
    
    except Exception as error:
        return f'Ошибка {error}'

print(send_email('toksonbaevislam2004@gmail.com', 'ДОЛГОЖДАННЫЙ LAST SUNDAY + ВЫПУСКНОЙ🎓', '''Дорогие студенты!
  
🗓В это воскресенье, 09 июня - состоится наш традиционный Last Sunday и Выпускной🚀
  

☝🏻Участвовать могут ТОЛЬКО студенты Geeks! 
Обязательно поставьте ➕ если придете! 
  
С уважением, администрация Geeks❤️'''))
