from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def hello():
    return Response("OKIDOKI", status=200, mimetype='application/json')      

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# application = flask.Flask(__name__)

# @application.route('/')
# def hello():
#     return Response("OKIDOKI", status=200, mimetype='application/json')      
 
# if __name__ == '__main__':
#     application.run(host='0.0.0.0')