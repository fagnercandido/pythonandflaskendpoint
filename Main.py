from flask import Flask

app = Flask(__name__)

@app.route('/info', methods = ['GET'])
def info():
    return 'This a simple endpoint to test and provides information about things.'

@app.route('/insert', methods = ['POST'])
def insert():
    return 'This a simple endpoint to test insert data.'

if __name__ == '__main__':
    app.run()
