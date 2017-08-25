from picamera import PiCamera
from gpiozero import Button
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



camera = PiCamera()
camera.vflip = True
button = Button(2)
num = 0
sender = 'pi@email.com'
server = "rservergoeshere"

print("PRESS THE BUTTON TO TAKE A PICTURE")

#button.wait_for_press()
while True:
        button.wait_for_press()
        camera.start_preview(alpha=192)
        sleep(1)
        camera.capture("openHouse{0}.jpg".format(num))
        camera.stop_preview()

        receiver = input("Please enter your email")

        filename = "openHouse{0}.jpg".format(num)
        
        


        SUBJECT = "Email Data"

        msg = MIMEMultipart()
        msg['Subject'] = "Open house picture" 
        msg['From'] = sender
        msg['To'] = receiver

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(filename, "rb").read())
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment; filename="'+filename+'"')

        msg.attach(part)

        server = smtplib.SMTP(server)
        server.sendmail(sender, receiver, msg.as_string())
        print("PRESS THE BUTTON TO TAKE A PICTURE")



