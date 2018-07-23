import smtplib as smtp

host = 'outbound.cisco.com'
port = 25
local_hostname = ''
sender = 'from@fromdomain.com'
receivers = ['yoav.e@quali.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
smtpObj = smtp.SMTP(host=host,
                    port=port,
                    local_hostname=local_hostname)

try:
    smtpObj = smtp.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except Exception as e:
    print "Error: unable to send email"
pass