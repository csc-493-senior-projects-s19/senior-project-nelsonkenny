import os,sys
from app.allImports import app
from flask import Flask
# app = Flask(__name__)
'''Insert the base location for the app in Cloud9'''
sys.path.insert(0,'/home/ubuntu/workspace/')

# Builds the server configuration
if os.getenv('IP'):
  IP = os.getenv('IP')
else:
  IP = '0.0.0.0'

if os.getenv('PORT'):
  pass
  # PORT = int(os.getenv('PORT'))
#else:
PORT = 8081

# Print statements go to your log file in production; to your console while developing
print ("Running server at http://{0}:{1}/".format(IP, PORT))
app.run(host = IP, port = PORT, debug = True, threaded = True)
