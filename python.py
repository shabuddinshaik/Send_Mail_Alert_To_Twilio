import win32com.client
from twilio.rest import Client
import schedule
import time
import logging

# Your Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Set up logging
logging.basicConfig(filename='twilio_Alert.logs', level=logging.INFO)

def check_email_and_send_alert():
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    inbox = namespace.Folders['your_email_address'].Folders['Inbox']
    messages = inbox.Items

    for message in messages:
        if message.UnRead and 'grafana' in message.SenderEmailAddress.lower():
            if 'level: critical' in message.Body.lower() or 'SEVERITY=HIGH' in message.Body:
                # Send SMS
                message = client.messages.create(
                    body="Critical alert received from Grafana. Details: " + message.Body,
                    from_='your_twilio_number',
                    to='your_phone_number'
                )

                # Make call
                call = client.calls.create(
                    twiml='<Response><Say>A critical alert was received from Grafana. Please check your email.</Say></Response>',
                    from_='your_twilio_number',
                    to='your_phone_number'
                )

                # Send email
                alert_email = outlook.CreateItem(0)
                alert_email.Subject = 'Critical Grafana Alert'
                alert_email.Body = 'A critical alert was received from Grafana. Details: ' + message.Body
                alert_email.To = 'your_email_address'
                alert_email.Send()

                logging.info('Alert sent successfully.')
                
                # Mark the message as read
                message.UnRead = False

# Schedule the job every 5 minutes
schedule.every(5).minutes.do(check_email_and_send_alert)

while True:
    schedule.run_pending()
    time.sleep(1)
