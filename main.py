from Bot import ChatBot as bot
from gettext import translation
import subprocess
import threading
from flask import Flask, render_template, request, jsonify
import os


bot = bot.ChatBot.getBot()

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = (request.form['messageText'])


    while True:
        if message == "":
            continue

        else:
            bot_response = str(bot.response(message))
            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})


#@app.route("/ask", methods=['POST'])
#def ask():
#    message = request.form['messageText']
#   ans = bot.get_response(message)
#   print(ans)
#   while True:
#       if message == "quit":
#           exit()
#       else:
#           class Object:
#               def __init__(self, status=None, answer=None):
#                    self.status = status
#                    self.answer = answer
#
#                def toJSON(self):
#                    return json.dumps(self, default=lambda o: o.__dict__, 
#            sort_keys=True, indent=4)
#            data = Object('OK', ans)
#            return data.toJSON()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

