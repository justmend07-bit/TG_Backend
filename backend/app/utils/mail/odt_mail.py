from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings 
import requests
import resend 
import base64
import os
conf = ConnectionConfig(
    MAIL_USERNAME= settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=settings.mail_starttls,
    MAIL_SSL_TLS=settings.mail_ssl_tls,
    USE_CREDENTIALS=settings.use_credentials,
)

resend.api_key = settings.resend_api_key
base_url = settings.base_url

# async def send_booking_email(data, image_path: str | None = None):
#     """Send booking details via Resend API with optional image attachment."""

#     email_body = f"""
#     Full Name: {data.full_name}
#     Email Address: {data.email_address}
#     Age: {data.age}
#     Gender: {data.gender}
#     Contact Number: {data.contact_number}
#     Whatsapp Number: {data.whatsapp_number}
#     College Name: {data.college_name}
#     Pick-up Location: {data.pick_up_loc}
#     Drop Location: {data.drop_loc}
#     Meal Preference: {data.meal_preference}
#     Experience Level: {data.trip_exp_level}
#     Medical Details: {data.medical_details}
#     Agree to Terms: {data.agree}
#     """

#     attachments = []

#     # ✅ Attach local file as Base64 (no 'path' key)
#     if image_path and os.path.exists(image_path):
#         with open(image_path, "rb") as f:
#             file_data = base64.b64encode(f.read()).decode("utf-8")
#             file_name = os.path.basename(image_path)
#             attachments.append({
#                 "content": file_data,
#                 "filename": file_name,
#                 "type": "image/jpeg" if image_path.lower().endswith((".jpg", ".jpeg")) else "image/png"
#             })

#     email = {
#         "from":  "Tirth Ghumo <onboarding@resend.dev>",
#         "to": ["tirthghumo@gmail.com"],
#         "subject": "New Trekking Package Booking",
#         "text": email_body.strip(),
#     }

#     # Only add attachments if present
#     if attachments:
#         email["attachments"] = attachments

#     try:
#         resend.Emails.send(email)
#         return {"status": "Email sent successfully"}
#     except Exception as e:
#         raise Exception(f"Email sending failed: {str(e)}")

async def send_booking_email(data, image_path: str | None = None):
    admin_action_base = f"{base_url}/odt/confirm"  # Base URL for admin actions

    button_739 = f"{admin_action_base}?booking_id={data.id}&amount=739"
    button_939 = f"{admin_action_base}?booking_id={data.id}&amount=939"

    html_body = f"""
    <h3>New Booking Received</h3>
    <p><b>Name:</b> {data.full_name}</p>
    <p><b>Email:</b> {data.email_address}</p>
    <p><b>Contact:</b> {data.contact_number}</p>
    <p><b>College:</b> {data.college_name}</p>

    <p><b>Select Package Amount:</b></p>

    <a href="{button_739}" 
       style="padding:10px 20px;background:#008CBA;color:white;text-decoration:none;border-radius:6px;">
       Approve ₹739
    </a>

    <a href="{button_939}" 
       style="padding:10px 20px;background:#4CAF50;color:white;text-decoration:none;border-radius:6px;margin-left:10px;">
       Approve ₹939
    </a>
    """

    attachments = []

    # ✅ Attach local file as Base64 (no 'path' key)
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            file_data = base64.b64encode(f.read()).decode("utf-8")
            file_name = os.path.basename(image_path)
            attachments.append({
                "content": file_data,
                "filename": file_name,
                "type": "image/jpeg" if image_path.lower().endswith((".jpg", ".jpeg")) else "image/png"
            })

    email = {
        "from": "Tirth Ghumo <onboarding@resend.dev>",
        "to": ["tirthghumo@gmail.com"],
        "subject": "New Trekking Package Booking",
        "html": html_body,
    }
    if attachments:
        email["attachments"] = attachments

    try:
        resend.Emails.send(email)
        return {"status": "Email sent successfully"}
    except Exception as e:
        raise Exception(f"Email sending failed: {str(e)}")

   


async def send_email_with_invoice(data, invoice_path):
    """Send invoice PDF to user using Resend"""

    # ---- Attach PDF ----
    with open(invoice_path, "rb") as f:
        file_bytes = base64.b64encode(f.read()).decode("utf-8")

    # ---- Email Body ----
    email_body = f"""
    Hi {data.full_name},

    Thank you for booking your trek with Tirth Ghumo!

    Your invoice is attached with this email.

    Regards,
    Team Tirth Ghumo
    """

    # ---- Email Payload ----
    email = {
        "from": "Tirth Ghumo <no-reply@tirthghumo.in>",
        "to": [data.email_address],
        "subject": "Your Trek Booking Invoice",
        "text": email_body.strip(),
        "attachments": [
            {
                "filename": "invoice.pdf",
                "content": file_bytes,
                "type": "application/pdf"
            }
        ]
    }

    # ---- Send ----
    try:
        resend.Emails.send(email)
    except Exception as e:
        raise Exception(f"Invoice email failed: {str(e)}")
