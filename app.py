from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Jungle.'

@app.route('/info')
def info():
    return 'This a simple endpoint to test and provides information about things.'

if __name__ == '__main__':
    app.run()
