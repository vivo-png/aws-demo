from flask import *


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return "Hello From Flask"
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    #serve(app)
    #host='0.0.0.0', port=8000
