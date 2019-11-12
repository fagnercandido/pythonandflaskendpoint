from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Jungle.'

@app.route('/info')
def info():
    return 'This a simple endpoint to test and provides information about things.'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
