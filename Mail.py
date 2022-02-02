import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj=MIMEMultipart()
x=input("alan mail :")
a=input("mesaj :")
mesaj["From"]="gönderen mail adresi"
mesaj["To"]=x
mesaj["Subject"]='Python ile mail atıyorum'
yazi=a

mesajGovdesi=MIMEText(yazi,"plain")
mesaj.attach(mesajGovdesi)
try:
    mail=smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
#mail adresi ve şifrenizle giriş yapın
    mail.login("mail adresi","şifresi")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    
    mail.close()
except:
    sys.stderr.write("mail göndeliremedi")
    sys.stderr.flush()
