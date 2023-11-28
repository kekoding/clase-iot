from flask import Flask, jsonify
import datetime
import Adafruit_DHT
import random

app = Flask(__name__)

@app.route('/temperatura', methods=['GET'])
def traer_temperatura(sensor=Adafruit_DHT.DHT11, pin=4):
    try:
        h, t = Adafruit_DHT.read(sensor, pin)
        if (t) is None:
            t = random.uniform(7.0, 14.5)
    except Exception as e:
        print(str(e))
        return jsonify({'msg':str(e)}), 500
    else:
        return jsonify({'temperatura':t, 'fecha_lectura':datetime.datetime.now(datetime.timezone.utc)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


