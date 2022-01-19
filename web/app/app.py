""" flask server app """
from flask import Flask, jsonify, render_template

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder="../static")


@app.route('/json')
def hello_world():
    """ Return a json message """
    return jsonify(message='Hello World!')


@app.route('/')
def hello_world2():
    """ Return a html output """
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
