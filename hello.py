from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/other')
def other_page():
    return 'Page Change!'

if __name__ == '__main__':
    app.run()
