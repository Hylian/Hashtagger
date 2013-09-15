from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/hashtag', methods=['POST', 'GET'])
def hashtag():
    if request.method=='POST':
        hashtag = request.form['hashtag']
        return render_template('hashtag.html', sentence='the hashtag is ' + hashtag)
    else:
        return 'You messed up'

app.debug = False
if __name__ == '__main__':
    app.run(debug=True)
