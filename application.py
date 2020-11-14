from flask import Flask, request, Response

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def hello():
    return Response("OKIOKI", status=200, mimetype='application/json')      

if __name__ == '__main__':
    app.run()

# application = flask.Flask(__name__)

# @application.route('/')
# def hello():
#     return Response("OKIDOKI", status=200, mimetype='application/json')      
 
# if __name__ == '__main__':
#     application.run(host='0.0.0.0')