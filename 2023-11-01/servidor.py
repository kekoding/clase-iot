import flask
from flask import jsonify, request, render_template
from servicios import mi_servicio

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return jsonify({
        'texto':"Hola!!"
    }), 200

@app.route('/cuadrado', methods=['GET'])
def cuadrado():
    num = request.args.get('num', default=0, type=int)
    if num > 0:
        return jsonify({
            'numero_original':num,
            'numero_cuadrado':num*num
        }), 200
    else:
        return jsonify({
            'error':"Favor de usar números mayores a 0"
        }), 401



if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0')