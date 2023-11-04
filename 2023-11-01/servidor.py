import flask
from flask import jsonify, request, render_template
from flask_cors import cross_origin, CORS
from servicios import leds

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

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
    
@app.route('/click', methods=['GET'])
def click():
    led_id = request.args.get('led_id', None, type=int)
    if led_id is None:
        return jsonify({
            'error':'Incluir parámetro LED ID!!'
        }), 405
    leds.click(led_id)
    return jsonify({
        'mensaje':f'Se desc/activo el led {led_id}'
    }), 200


@app.route('/status', methods=['GET'])
@cross_origin()
def status():
    return jsonify({
        'data':leds.regresa_todos_status()
    })


if __name__ == '__main__':
    app.run(port=5500, host='localhost')