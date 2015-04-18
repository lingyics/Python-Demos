'''
Sending Emails using Python is Simple and Efficient
We could send text, html, attachment,image, audio and ect
Simple sample code
Sending Group Emails
'''

import os
import os.path
import sys
from ftplib import FTP
import zipfile
from zipfile import *
import shutil
import time
from datetime import datetime
import MySQLdb
import MySQLdb.cursors
import csv
import glob
import decimal
import getpass


import time
import datetime
from datetime import datetime
from time import strptime, strftime
from datetime import date, timedelta

# this is the Library we use
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = "XXX@gmail.com"
emailto = ["XXX@gmail.com","XXX@gmail.com"]
username = "XXXX"
password = "XXXXX"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = ";".join(emailto) #using join for multiple emails
msg["Subject"] = "Sending Group Emails with Attachments! "
msg.preamble = “Hello~~ World~~~”

def attach_files(fileToSend):
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)


    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)

    msg.attach(attachment)

def send_mail(files):


    for f in files:
        attach_files(f)
    
    text = "this it the text"
    html = """\
    <html>
        <head></head>
        <body>
            <p>Hi!<br>
                How are you?<br>
                Here is the <a href="https://www.python.org">link</a> you wanted.
            </p>
        </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred

    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP("smtp.gmail.com:587") #587 for gmail host
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()





if __name__=="__main__":
    files=["/PathToFile1/file1","/PathToFile2/file2"]
    send_mail(files)



