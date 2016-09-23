from flask import Flask, jsonify
from flask import make_response
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


@app.route('/api/get', methods=['GET'])
def get():
    _id = request.args['id']
    name = request.args['name']
    data = {'id': _id, 'name': name}
    return jsonify(data)


@app.route('/api/post', methods=['POST'])
def post():
    _id = request.form['id']
    name = request.form['name']
    data = {'id': _id, 'name': name}
    return jsonify(data)


@app.route('/api/gp', methods=['GET', 'POST'])
def gp():
    _id = request.values['id']
    name = request.values['name']
    data = {'id': _id, 'name': name}
    resp = make_response(jsonify(data), 200)
    resp.headers['X-My-Header'] = 'my value'
    return resp


if __name__ == '__main__':
    app.run()
