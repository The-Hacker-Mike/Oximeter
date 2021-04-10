
# API de servicios
import os
import time
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
from twilio.rest import Client
import db_connector as db


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})

# change configuration variables
account_sid = ''
auth_token = ''

class MESSAGE(Resource):

    def post(self):
        # break into smaller parts the information of the message:
        req = request.json

        number = request.form['From'] # from the message "from" is obtained, which is my phone number.
        message_body = request.form['Body'].lower() # lower is used to convert the message to low case letters only.
        mensaje = ""

        client = Client(account_sid, auth_token)

        if message_body.find("heart rate") == 0:
          db.create_img(number)   # comment this line of code after a new phone number is introduced not before.
          mensaje = " "+ db.find_user(number) + " esta es la informacion actual de tus registros"
          print(number)
          message = client.messages.create (
                                      from_ = '',
                                      body = mensaje,
                                      # update ngrok id
                                      media_url = [''+number],
                                      to = number
                                  )
        else:
          try:
            mensaje = "Hola "+db.find_user(number)+ " puedes pedirme tu Heart Rate por el momento."
            message = client.messages.create (
                                    from_ = '',
                                    body = mensaje,
                                    to = number
                                )

          except:
            mensaje = "No estas registrado. Escribe ->  Nombre: Nombre y Apellido  <- todo junto por favor"
            message = client.messages.create (
                                    from_ = '',
                                    body = mensaje,
                                    to = number
                                )

class IMAGE(Resource):
    def get(self):
        number = request.args.get('number')
        number = number.replace(": ","_+")
        print(number)
        filename = number + '.png'
        return send_file(filename, mimetype = 'image/png')

api.add_resource(MESSAGE, '/message')  # Route_1 Me -> Post
api.add_resource(IMAGE, '/image')  # Route_2 GET

if __name__ == '__main__':
    app.run(port = '')
