from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
 
emailMsg = 'You won $100,000'
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'nextin.520@gmail.com'
mimeMessage['subject'] = 'You won'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
 
message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
#print(message)

def email(Msg , email , subject):
    emailMsg = Msg
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    html_body_tag = "<body>-------</body>"
    msg.attach(TexT(html_body_tag , 'html'))
    
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
