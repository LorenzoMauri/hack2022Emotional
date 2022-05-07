from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return f"<p>{dictToReturn}KJHHFUIFDHUIFDHFSDIUDFUIFDHF</p>"




if __name__ == '__main__':
    app.run(host='127.0.0.1', port='4000', debug=True)