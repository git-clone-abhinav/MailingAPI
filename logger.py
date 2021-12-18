import time
from dotenv import load_dotenv
load_dotenv()
logPath = os.getenv('logs')
def logit(message):
    with open(logPath, 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()