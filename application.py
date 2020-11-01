import flask
from flask import request, Response

application = flask.Flask(__name__)

@application.route('/')
def hello():
    return Response("OKIDOKI", status=200, mimetype='application/json')      
 
if __name__ == '__main__':
    application.run(host='0.0.0.0')