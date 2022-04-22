from re import T
from smtplib import SMTP
from email.message import EmailMessage

class Sending:
    def __init__(self) -> None:
        self.EMAIL = "smtptestingforomc@gmail.com"
        self.PASSWORD = "@]~#+564dSqs5DZd4sq6DCdea"
        self.SERVER = "smtp.gmail.com"
        self.PORT = 587

    def acceptance(self,id ,email , club, subject= None) -> None:
        # connect to server and send an email using a template
        server = SMTP(f"{self.SERVER}:{self.PORT}")
        email = "email@email.com"
        try:server.starttls()
        except:pass
        server.ehlo()
        server.login(self.EMAIL,self.PASSWORD)

        # changing content of templates
        index = open("templates/html/accept.html")
        emailContent = index.read()
        emailContent = emailContent.replace("[ID]",id)
        emailContent = emailContent.replace("[CLUBNAME]",club)
        emailContent = emailContent.replace("[SUBJECT]",subject)
        
        # setting up MIME
        msg = EmailMessage()
        msg['from'] = f"no-reply <{self.EMAIL}>"
        msg["subject"] = f"Request Accepted ! [{id}]"
        msg.add_alternative(emailContent,"html")
        
        # sending mail
        server.sendmail(msg["from"],email,msg.as_string().encode("utf-8"))
        server.close()
        
    def denial(self,id ,email , club, subject= None) -> None:
        # connect to server and send an email using a template
        server = SMTP(f"{self.SERVER}:{self.PORT}")
        email = "email@email.com"
        try:server.starttls()
        except:pass
        server.ehlo()
        server.login(self.EMAIL,self.PASSWORD)

        # changing content of templates
        index = open("templates/html/denied.html")
        emailContent = index.read()
        emailContent = emailContent.replace("[ID]",id)
        emailContent = emailContent.replace("[CLUBNAME]",club)
        emailContent = emailContent.replace("[SUBJECT]",subject)
        
        # setting up MIME
        msg = EmailMessage()
        msg['from'] = f"no-reply <{self.EMAIL}>"
        msg["subject"] = f"Request Denied. [{id}]"
        msg.add_alternative(emailContent,"html")
        
        # sending mail
        server.sendmail(msg["from"],email,msg.as_string().encode("utf-8"))
        server.close()

