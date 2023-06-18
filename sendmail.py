import smtplib
import argparse
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def send_mail(subject, message, smailid, app_secret, tmailid):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    receiver = tmailid
    sender = smailid
    sender_pass = app_secret
    s.login(sender, sender_pass)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = smailid
    msg['To'] = tmailid
    html_content = MIMEText(message, 'html')
    msg.attach(html_content)

    # sending the mail
    s.sendmail(sender, receiver, msg.as_string())
    
    # terminating the session
    s.quit()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-smail", "--smail", required=True,help="source email address")
    ap.add_argument("-tmail", "--tmail", required=True,help="target email address")
    ap.add_argument("-subject", "--subject", required=True,help="Subject for email")
    ap.add_argument("-message", "--message", required=True,help="Message content for email")
    ap.add_argument("-ssecret", "--ssecret", required=True,help="App secret for source mail id")
    ap.add_argument("-file_path", "--file_path", required=True,help="File Path for the attachment")
    args = vars(ap.parse_args())
    smailid = str(args['smail']).lower()
    tmailid = str(args['tmail']).lower()
    subject = str(args['subject'])
    message = str(args['message'])
    app_secret = str(args['ssecret'])
    file_path = str(args['file_path'])
    send_mail(subject, message, smailid, app_secret, tmailid)


