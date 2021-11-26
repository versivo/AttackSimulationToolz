#!/usr/bin/env python3

import smtplib
import yaml
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('config.yaml', 'r') as stream:
    try:
        vars = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)
        sys.exit(1)

for you in vars['destinations']:
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = vars['from']
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = f"""\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
        <img width="1" heigth="1" src="{vars['tracker']}?{you}" />
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP(vars['smtp_relay_host'], vars['smtp_relay_port'])
    s.starttls() # Secure the connection
    s.login(vars['smtp_relay_username'], vars['smtp_relay_password'])

    # s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(vars['from'], you, msg.as_string())
    s.quit()
    
