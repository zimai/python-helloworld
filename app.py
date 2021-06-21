from flask import Flask
from flask import json
#import logging
from logging.config import fileConfig

app = Flask(__name__)

#logging.basicConfig(filename='app.log', level=logging.DEBUG)
fileConfig('logging.cfg')

@app.route("/")
def hello():
    app.logger.info('Main request successful')
    
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.debug('Status request successful')
    
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successful')
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
