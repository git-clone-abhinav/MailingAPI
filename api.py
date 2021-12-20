from flask import Flask, request, jsonify,send_file, redirect,session, url_for
import logger
import mailer
import os
from flask_cors import CORS, cross_origin
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()

path = os.getenv('upload_folder')
logpath = os.getenv('logs')
lists = os.getenv('lists')

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return "Hallo There"

'''
Mail request headers
uname
password
tolist
sub
msg
'''

@app.route("/send_mail")
def send_mail():
   uid = request.args.get('uid')
   pwd = request.args.get('pwd')
   tolist = request.args.get('tolist')
   sub = request.args.get('sub')
   msg = request.args.get('body')
   logger.log_it(f"{uid}  - {tolist} - {sub} - {msg}")
   mailer.mail(uid,pwd,tolist,sub,msg)
   return "done"

@app.route('/logs')
def logs():
   with open(logpath,"r") as f:
      lines = f.readlines()
      f.close()
   formated_lines = []
   for i in range(len(lines)-1,0,-1):
      formated_lines.append(lines[i])
   return jsonify({'logs':formated_lines})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 2000,debug = True)