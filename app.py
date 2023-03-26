from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello')
@swag_from('swagger.yaml', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/add')
@swag_from('swagger.yaml', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)
