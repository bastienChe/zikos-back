from flask import Flask, request, Response

application = Flask(__name__)
application .debug = True

@application .route('/', methods=['GET'])
def hello():
    return Response("OKIOKI", status=200, mimetype='application/json')      

if __name__ == '__main__':
    application .run()

# application = flask.Flask(__name__)

# @application.route('/')
# def hello():
#     return Response("OKIDOKI", status=200, mimetype='application/json')      
 
# if __name__ == '__main__':
#     application.run(host='0.0.0.0')