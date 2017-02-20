# server.py
import time

HOST = '127.0.0.1'
PORT = '4444'

url = 'tcp://{}:{}'.format(HOST, PORT)


from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/downcase/", methods=['GET'])
def lowerString():
 _strn = request.args.get('param')
 response = 'lower case of {} is {}'.format(_strn, _strn.lower())
 return response

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=False)
