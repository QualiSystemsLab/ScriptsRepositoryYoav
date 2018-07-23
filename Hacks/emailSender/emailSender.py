import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import cloudshell.api.cloudshell_api as api
import json
reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
# resource_context = json.loads(os.environ['RESOURCECONTEXT'])
connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])

class email_sender():
    def __init__(self):
        pass

    def _email(self, smtp_server, smtp_port, tls, from_name, to_address, msg):
        smtp = smtplib.SMTP(host=smtp_server, port=int(smtp_port))
        if tls:
            smtp.starttls()
        smtp.sendmail(from_addr=from_name, to_addrs=to_address, msg=msg.as_string())
        smtp.close()

    def _send_email(self, smtp_server, smtp_port, from_name, to_address, subject, tls, message, is_html):
        msg = MIMEMultipart('alternative')
        msg['From'] = from_name
        msg['To'] = ';'.join(to_address)
        msg['Subject'] = subject
        if is_html:
            mess = MIMEText(message, 'html')
        else:
            mess = MIMEText(message, 'plain')
        msg.attach(mess)
        try:
            self._email(smtp_server, smtp_port, tls, from_name, to_address, msg)
        except Exception, _exp:
            raise Exception(str(_exp))

    def send(self):
        emails = os.environ["recipients"].split(";")
        user_subject, user_message = self.create_HTML()
        self._send_email(
            smtp_server='outbound.cisco.com',
            smtp_port='25',
            from_name='Quali-Server@cisco.com',
            to_address=emails,
            subject=user_subject,
            message=user_message,
            tls=True,
            is_html=True
        )

    def create_HTML(self):
        session = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
                                           token_id=connectivity_details['adminAuthToken'],
                                           domain=reservation_details['domain'])
        all_resources = session.GetReservationDetails(reservation_details['id']).ReservationDescription.Resources
        res_end_time = session.GetReservationDetails(reservation_details['id']).ReservationDescription.EndTime
        for a_resource in all_resources:
            if a_resource.ResourceModelName == 'vRouter Virtual Machine':
                router_ip = a_resource.FullAddress
        subject = 'R00tCamp POD - Reservation ID {0}'.format(reservation_details['id'])
        html_message = '''
        <html>
        <head></head>
        <body>
        <h1>R00TCAMP REMOTE ACCESS DETAILS</h1>
        <h3>Reservation will end in '''+ res_end_time +'''</h3>
        <h2>SUT Details: </h2>
        <p>No Machine -> ''' + router_ip +''' : 9003</p>
        <p>SSH -> ''' + router_ip +''': 9002</p>
        <h2>KALI Details: </h2>
        <p>No Machine -> ''' + router_ip +''' : 9001 </p>
        <p>SSH -> ''' + router_ip +''' : 9000 </p>
        <h2>Win7 Details: </h2>
        <p>No Machine -> ''' + router_ip +''' : 9004 </p>
        <p>to access your reservation ,
        <a href="https://qs.cisco.com/RM/Diagram/Index/'''+ reservation_details['id'] +'''">click here</a></p>
        </body>
        </html>
        '''
        return subject, html_message