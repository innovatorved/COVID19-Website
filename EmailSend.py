from ConnectGoogle import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from CoronaData import done

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def email(name , email):
    #emailMsg = Msg
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email
    mimeMessage['subject'] = "Registration Successfull"
    
    #mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    html_body_tag = "<body style='text-align: center;'>"+"<img src= "+'https://i.ibb.co/cJwWmsK/coronavirus.png'+"width='150' height='150'>"+"</br></br></body>"
    mimeMessage.attach(MIMEText(html_body_tag , 'html'))
    
    mimeMessage.attach(MIMEText("<div style='text-align: center;' >\n<h2>Dear "+name+",</h2><h3>\nDone ,You Are Successfully Registered \nwith Corona Update App<h3><br><h4>\nThank you ,team CoronaUpdate</h4><div>" , 'html'))
    
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()



def send(link , mail):
    """

    two parameter passes list of three links and email id
    cmd for send cases data to Email


    """
    link1 = link[0]
    link2 = link[1]
    link3 = link[2]
    
    link4 = link[3]
    link5 = link[4]
    
    #emailMsg = Msg
    Message = MIMEMultipart()
    Message['to'] = mail
    Message['subject'] = "Today Corona Data"
    
    #mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    html_body_tag = "<body style='text-align: center;'>"+"<img src= "+'https://i.ibb.co/cJwWmsK/coronavirus.png'+"width='150' height='150'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))
    
    html_body_tag = "<body style='text-align: center;'>"+"<h2>Active Cases</h2><img src= "+link1+"width='250' height='250'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))

    html_body_tag = "<body style='text-align: center;'>"+"<h2>Recovered Cases</h2><img src= "+link2+"width='250' height='250'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))

    html_body_tag = "<body style='text-align: center;'>"+"<h2>All Detail - Pie Chart</h2><img src= "+link3+"width='250' height='250'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))
    

    html_body_tag = "<body style='text-align: center;'>"+"<h2>Plot</h2><img src= "+link4+"width='250' height='250'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))

    html_body_tag = "<body style='text-align: center;'>"+"<h2>Covid19 Prediction</h2><img src= "+link5+"width='250' height='250'>"+"</br></br></body>"
    Message.attach(MIMEText(html_body_tag , 'html'))


    html_body_tag = "<body style='text-align: center;'>"+"<br><br>If You Want to Unsubscribe from CoronaUpdate WebApp<br>Send 'Unsubscribe' at<br>coronaupdate.now@gmail.com</body>"
    Message.attach(MIMEText(html_body_tag , 'html'))

    raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()



