from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import DictCursor
import datetime
from dataclasses import dataclass

DSN =  'dbname=postgres user=postgres password=postgres host=localhost port=5432'
@dataclass
class DatoTemperatura:
    temperatura : float
    fecha_lectura : datetime.datetime

app = Flask(__name__)

@app.route('/temperatura_actual', methods=['GET'])
def temperatura_actual():
    try:
        with psycopg2.connect(DSN) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("select temperatura from temperatura order by fecha_lectura desc limit 1")
                datos = cur.fetchall()
                data : list[dict] = [dict(row) for row in datos]
                temperatura : float = data[0].get("temperatura")
    except Exception as e:
        print(str(e))
    else:
        return jsonify({'temperatura':temperatura}), 200
    
@app.route('temperatura_promedio', methods=['GET'])
def temperatura_promedio():
    # TODO
    sql = f'''\
        select avg(temperatura) as temperatura_promedio, 
        extract(minute from fecha_lectura) as minuto
        from temperatura
        group by extract(minute from fecha_lectura)
        order by minuto desc
    '''
