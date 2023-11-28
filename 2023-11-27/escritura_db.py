from dataclasses import dataclass
import datetime
import requests
import psycopg2

URL = 'http://raspberrypi.local:8000'
DSN =  'dbname=postgres user=postgres password=postgres host=localhost port=5432'

@dataclass
class DatoTemperatura:
    temperatura : float
    fecha_lectura : datetime.datetime


def escribir_db_temp():

    try:
        res = requests.get(url=URL+'/temperatura')
        assert res.status_code == 200, f'No fue posible llamar al servicio'
        datos : dict = res.json()
        datos : DatoTemperatura = DatoTemperatura(**datos)
        conn, cur = None, None

        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = f'''\
                insert into temperatura (temperatura, fecha_lectura)
                values (%s, %s)
            '''
        cur.execute(sql, vars=(datos.temperatura, datos.fecha_lectura))
        if cur.rowcount > 0:
            conn.commit()
        else:
            conn.rollback()
    except Exception as e:
        pass
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    while True:
        escribir_db_temp()