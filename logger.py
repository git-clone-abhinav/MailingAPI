import time
import os
from dotenv import load_dotenv

load_dotenv()
logPath = os.getenv('logs')
def log_it(message):
    with open(logPath, 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()