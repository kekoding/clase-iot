from flask import jsonify, request, render_template, Flask
from flask_cors import CORS, cross_origin
from servicios import leds
from gpiozero import LED

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

led = LED(14)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route('/led', methods=['GET'])
def click():
    leds.click_led(led)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
