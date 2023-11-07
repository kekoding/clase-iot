from flask import jsonify, request, render_template, Flask
from servicios import leds

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route('/led', methods=['GET'])
def click():
    if 'npin' not in request.args.keys():
        return 'INGRESA NPIN!!'
    numero_pin = request.args.get('npin', default=0, type=int)
    print(f"el número de pin es {numero_pin}")
    leds.click_led()
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
