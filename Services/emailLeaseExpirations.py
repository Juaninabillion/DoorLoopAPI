import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from Clients.client import DoorLoopClient
from data.Import.sentLeasesTracker import insert_lease_to_datesent_table
from data.Extract.commercial_lease_expirations import fetch_commercial_expiring_leases 
from data.Extract.residential_lease_expirations import fetch_residential_expiring_leases
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
# Gmail SMTP config
smptserver = os.getenv("SMTP_SERVER")
smpt_port = os.getenv("SMTP_PORT")
smptuser = os.getenv("GMAIL_USER")
smptpass = os.getenv("GMAIL_PASSWORD")
lease_url = os.getenv("DOORLOOP_LEASE_URL")
send_email = os.getenv("SEND_EMAIL", "FALSE")
lease_tracker = []
api_key = os.getenv("DOORLOOP_API_KEY")
resiEmail = os.getenv("RESIDENTIAL_EMAIL", "")
comEmail = os.getenv("COM_EMAIL", "")
ccEmail = os.getenv("CCEMAIL","")




def send_email(subject, body, to_email):
    if send_email == "False":
        print("Email sending is disabled.")
        return
    else:
        print("Sending email...")
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = smptuser
        msg["To"] = to_email
        msg["Cc"]=ccEmail
        html_part = MIMEText(body, "html")
        msg.attach(html_part)

        # If you want to send HTML content

        with smtplib.SMTP(smptserver, smpt_port) as smtp:
            smtp.starttls()
            smtp.login(smptuser, smptpass)
            smtp.send_message(msg)
            print(f"Email sent: {subject}")
def inser_lease_tracker(lease_number):
    insert_lease_to_datesent_table(lease_number)

def main():
    
    
    for propclass in ["Residential", "Commercial"]:
        if propclass == "Residential":
            leases = fetch_residential_expiring_leases()
            email_to = resiEmail
        else:
            leases = fetch_commercial_expiring_leases()
            email_to = comEmail
        if len(leases) == 0:
            print(f"No {propclass.lower()} leases expiring.")
            continue
        else:
            print(f"Found {len(leases)} {propclass.lower()} leases expiring.")
            for lease in leases: 
                property_address = lease.get("PropertyName", "Missing Address")
                unit_name = lease.get("UnitName", "Missing Unit")
                unit_address = lease.get("UnitAddress", "Missing Unit Address")
                lease_end_date = lease.get("EndDate", "Missing End Date")
                lease_number = lease.get("LeaseNumber", "Missing Lease Number")

                subject = f"{property_address} Unit:{unit_name} - {propclass} Lease Expiring: {lease_end_date}"

                lurl = f"{lease_url}{lease_number}/overview"
                hyperlink_for_lease = f'<a href="{lurl}">here</a>'

                html_body = f"""
                <p>Dear Team,</p>
                <p>Please note that the {propclass.lower()} lease for <strong>{unit_name}</strong> at <strong>{unit_address}</strong> is expiring on <em>{lease_end_date}</em>.</p>
                <p>Find Lease information {hyperlink_for_lease}.</p>
                <p>Regards,<br>Alpha Engineering Team</p>
                """

                print(subject)
                print(html_body)
                #send_email(subject, html_body, email_to)  # Replace with actual recipient
                lease_tracker.append(lease_number)
                print(f"Lease {lease_number} processed for email notification.")
                inser_lease_tracker(lease_number)
        

            

        


if __name__ == "__main__":
    main()