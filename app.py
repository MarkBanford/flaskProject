from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'mark'}
    return 'Hi, ' + user['username']


if __name__ == '__main__':
    app.run(debug=True)
