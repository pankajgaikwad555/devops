from flask import Flask
import socket
import datetime

app = Flask(__name__)
@app.route('/')
def hellow_world():
  hostname = socket.gethostname()
  time = datetime.datetime.now().strftime("%m/%d/%y,%H:%M:%S")
  return 'Welcome from '+hostname+', at'+time

if __name__ == '__main__':
  app.run('0.0.0.0','5000')
