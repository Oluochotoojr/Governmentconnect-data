from flask import Flask, request
from africastalking import AfricasTalking

app = Flask(__name__)

# Configure Africa's Talking API credentials
username = "SteveOtoo"
api_key = "ec349041b1ad8c2e11ae40c4c1457d8ab964fea82479c7b844f6dbc9960b8eea"
africastalking = AfricasTalking(username, api_key)
sms = africastalking.sms

@app.route('/incoming', methods=['POST'])
def incoming_sms():
    message = request.json
    from_number = message['from']

    send_sms("Welcome to Government Connect", from_number)

    return "OK"

def send_sms(message, to):
    sms.send(message, [to])

if __name__ == "__main__":
    app.run(debug=True)
