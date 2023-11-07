from flask import jsonify, request, render_template, Flask
from flask_cors import CORS, cross_origin
from servicios import leds
from gpiozero import LED

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

diccionario =  {
    'verde':LED(14),
    'azul':LED(15)
}

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route('/led', methods=['GET'])
def click():
    nombre_led = request.args.get('led', default='', type=str)
    if nombre_led not in diccionario.keys():
        return "Solo se permiten azul o verde para el parámetro led"
    led = diccionario.get(nombre_led)
    print(f'El led {led} fue seleccionado por la llave {nombre_led}')
    msg : str = leds.click_led(led)
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
