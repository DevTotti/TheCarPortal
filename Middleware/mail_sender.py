import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests
import datetime
import os
load_dotenv()



car_portal_mail = os.environ["CAR_PORTAL_MAIL"]
car_portal_mail_password = os.environ["CAR_PORTAL_MAIL_PWD"]
car_portal_mail_gun_api_key = os.environ["MAIL_GUN_API_KEY"]
car_portal_mail_gun_username = os.environ["MAIL_GUN_USERNAME"]
car_portal_mail_gun_password = os.environ["MAIL_GUN_PASSWORD"]

def send_mail_google_smtp(cart_id, delivery, name, mail, phone):
    current_date = datetime.datetime.now().date()
    next_three_days = current_date + datetime.timedelta(days=3)

    mail_content = """
            Hi {name}, your order has been received.
 
            Order No.: {cart_id}
            Order date: {current_date}
            Estimated delivery date: {next_three_days}
            
                
            
            DELIVERY DETAILS

                DELIVERY ADDRESS
            
                {name}
                {delivery}
                {phone}

                
            DELIVERY METHOD
            
                GIG Motors

            If You would like the delivery address to change to another location, please reply this email with your prefered address

            Regards,
            The Car Portal Team
            www.thecarportal.net
            thecarportalnet@gmail.com
        """.format(name=name, cart_id=cart_id, delivery=delivery, phone=phone, current_date=current_date, next_three_days=next_three_days)

    sender_address = car_portal_mail
    sender_pass = car_portal_mail_password
    receiver_address = mail

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'THE CAR PORTAL ORDERED RECEIVED!'
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    # session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    ssl_context = ssl.create_default_context()
    session = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_context) #use gmail with port
    # session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent by Google')

    return 


def send_mail_gun_smtp(cart_id, delivery, name, mail, phone):
    current_date = datetime.datetime.now().date()
    next_three_days = current_date + datetime.timedelta(days=3)

    mail_content = """
        Hi {name}, your order has been received.

        Order No.: {cart_id}
        Order date: {current_date}
        Estimated delivery date: {next_three_days}
        
            
        
        DELIVERY DETAILS

            DELIVERY ADDRESS
        
            {name}
            {delivery}
            {phone}

            
        DELIVERY METHOD
        
            GIG Motors

        If You would like the delivery address to change to another location, please reply this email with your prefered address

        Regards,
        The Car Portal Team
        www.thecarportal.net
        thecarportalnet@gmail.com
    """.format(name=name, cart_id=cart_id, delivery=delivery, phone=phone, current_date=current_date, next_three_days=next_three_days)

    sender_address = "The Car Portal Crew <orders@thecarportal.net>"
    sender_pass = car_portal_mail_password
    receiver_address = mail


    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'THE CAR PORTAL ORDERED RECEIVED!'
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.mailgun.org', 587)

    session.login(car_portal_mail_gun_username, car_portal_mail_gun_password)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent by MailGun')

    return




# def send_mail_api(cart_id, delivery, name, mail, phone):
#     # Grab your SMTP credentials:
#     # SMTP hostname: smtp.mailgun.org
#     # Port: 587 (recommended)
#     # Username: postmaster@sandboxfcd2c51c0c904521a3fc830961b5be09.mailgun.org
#     # Default password: d49122f6d7f5b43b83c4d9bc821fea0c-e31dc3cc-5a43095f
#     domain = "https://api.mailgun.net/v3/thecarportal.herokuapp.com/messages"
#     sender =  "The Car Portal Crew <orders@thecarportal.net>"
    
#     current_date = datetime.datetime.now().date()
#     next_three_days = current_date + datetime.timedelta(days=3)

#     mail_content = """
#         Hi {name}, your order has been received.

#         Order No.: {cart_id}
#         Order date: {current_date}
#         Estimated delivery date: {next_three_days}
        
            
        
#         DELIVERY DETAILS

#             DELIVERY ADDRESS
        
#             {name}
#             {delivery}
#             {phone}

            
#         DELIVERY METHOD
        
#             GIG Motors

#         If You would like the delivery address to change to another location, please reply this email with your prefered address

#         Regards,
#         The Car Portal Team
#         www.thecarportal.net
#         thecarportalnet@gmail.com
#     """.format(name=name, cart_id=cart_id, delivery=delivery, phone=phone, current_date=current_date, next_three_days=next_three_days)

#     send = requests.post(
#         domain,
#         auth=("api", car_portal_mail_gun_api_key),
#         data={
#             "from": sender,
#             "to": [mail, car_portal_mail],
#             "subject": 'THE CAR PORTAL ORDERED RECEIVED!',
#             "text": mail_content
#             }
#         )

#     print(send)
