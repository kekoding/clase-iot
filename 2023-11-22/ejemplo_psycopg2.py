import psycopg2
from psycopg2 import extras

def insertar_empleado(id_empleado:int, nombre_empleado:str, apellido_empleado:str):
    try:
        # Connect to an existing database
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=localhost port=5432")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        sql = f'''\
            insert into empleados (id_empleado, nombre_empleado, apellido_empleado)
            values (%s, %s, %s)
        '''
        cur.execute(sql, vars=(id_empleado, nombre_empleado, apellido_empleado))
        assert cur.rowcount > 0
    except Exception as e:
        conn.rollback()
        print(str(e))
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

def traer_empleados():
    try:
        # Connect to an existing database
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=localhost port=5432")

        # Open a cursor to perform database operations
        cur = conn.cursor(cursor_factory=extras.DictCursor)

        cur.execute("SELECT * FROM empleados;")

        data = cur.fetchall()
    except Exception as e:
        print(str(e))
    else:
        return [dict(row) for row in data]
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    nuevo_empleado = {
        "id_empleado":11111,
        "nombre_empleado":"Juan",
        "apellido_empleado":"Gómez"
    }
    insertar_empleado(**nuevo_empleado)
    empleados = traer_empleados()
    pass