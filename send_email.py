import win32com.client
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import json
import urllib.request
import datetime
import smtplib,ssl
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from skimage import io
import cv2



r = requests.get("https://dog.ceo/api/breeds/image/random")
data = r.json()
url= data["message"]


print( "downloading %s" % (url))


with urllib.request.urlopen(url) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')

img.show()

email_login = ""   #introduce your email
email_pass_login = ""  #introduce your password

server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
server.starttls()
server.ehlo()
server.login(email_login, email_pass_login)

server.ehlo()

print ('server working fine')


sender = ""  #introduce the sender email

receivers = [""]   #introduce the list of receivers


message = MIMEMultipart()

message["From"]= sender
message["To"] = receivers[0]
message["Subject"]= "Prueba"



fp = open('temp.jpg', 'rb')
message.attach(MIMEImage(fp.read()))          # body of the email

text = message.as_string()


server.sendmail(sender, receivers, text)

print ('sending email to outlook')


server.quit()