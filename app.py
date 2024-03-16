from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['POST'])
def bot():
  number = request.form.get('From')

  try:
    from twilio.rest import Client

    account_sid = 'AC676d8e071ce0ea4839865a3c45e13968'
    auth_token = '2030f5127c1f1c7f2daa060246d511fb'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body='Sua mensagem foi recebida',
      to='whatsapp:+258844236139'
    )

    print(message.sid)
    return jsonify({'message': 'Success'})

  except Exception as e:
    return jsonify({'message': 'error'})



if __name__ == "__main__":
  app.run()