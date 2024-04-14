from flask import Flask, render_template, request, jsonify
import smtplib
import ssl
import os

app = Flask(__name__)

# Set the template folder explicitly
template_dir = os.path.abspath(os.path.dirname(__file__))
app.template_folder = os.path.join(template_dir)

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)
        
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, email_message)
        print("Email sent successfully")

@app.route('/send_email', methods=['POST'])
def handle_send_email():
    data = request.json
    sender_email = data['sender_email']
    sender_password = data['sender_password']
    recipient_email = data['recipient_email']
    subject = data['subject']
    message = data['message']

    send_email(sender_email, sender_password, recipient_email, subject, message)
    return jsonify({"message": "Email sent successfully"}), 200

@app.route('/')
def index():
    return render_template('alert.html')

#if __name__ == '__main__':
    #app.run(debug=True)
