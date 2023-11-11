from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# WhatsApp number and file path
whatsapp_number = 'whatsapp:+14155238886'  # Twilio's WhatsApp number
file_path = 'path_to_your_file/your_file.txt'  # Replace with the actual file path

# Send file
message = client.messages.create(
    body='Sending a file via WhatsApp Business API',
    from_='whatsapp:+1234567890',  # Your Twilio WhatsApp-enabled number
    media_url=['file://' + file_path],
    to=whatsapp_number
)

# Print the message SID
print(f"Message SID: {message.sid}")
