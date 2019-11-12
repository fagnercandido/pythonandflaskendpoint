from flask import Flask

app = Flask(__name__)

@app.route('/info', methods = ['GET'])
def info():
    return 'This a simple endpoint to test and provides information about things.'

@app.route('/insert', methods = ['POST'])
def insert():
    return 'This a simple endpoint to test insert data.'

@app.route('/', methods = ['GET'])
def index():
    return 'Welcome to the Jungle.'

if __name__ == '__main__':
    app.run()
