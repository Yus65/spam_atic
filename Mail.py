import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj=MIMEMultipart()
x=input("alan mail :")
a=input("mesaj :")
c=input("kaçtane :")
mesaj["From"]=""
mesaj["To"]=x
mesaj["Subject"]="spam"
yazi=a

mesajGovdesi=MIMEText(yazi,"plain")
mesaj.attach(mesajGovdesi)
try:
    mail=smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("mail adresi","şifresi")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    
    mail.close()
except:
    sys.stderr.write("saldırı başarısız")
    sys.stderr.flush()