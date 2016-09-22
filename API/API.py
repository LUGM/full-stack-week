from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yolo')
@app.route('/hello', methods=['GET'])
def hello():
    return 'This works with get only'


@app.route('/phello', methods=['GET', 'POST'])
def hello_post():
    if request.method == 'POST':
        return 'Its a post'
    else:
        return 'Its a get'


@app.route('/param/<int:name>', methods=['GET'])
def params(name):
    return name


@app.route('/static', methods=['GET'])
def statp():
    return app.send_static_file('test.html')


@app.route('/dynamic/<string:value>', methods=['GET'])
def dyanp(value):
    return render_template('temp.html', temp=value)


if __name__ == '__main__':
    app.run()
