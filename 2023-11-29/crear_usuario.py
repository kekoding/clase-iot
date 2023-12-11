from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import DictCursor
import os
import bcrypt
import uuid

# Para variables de ambiente
# Se puede usar la libreria dotenv

app = Flask(__name__)

DSN = f'dbname={os.getenv("DB_NAME")} user={os.getenv("DB_USER")} password={os.getenv("DB_PWD")} host={os.getenv("DB_HOST")} port={os.getenv("DB_PORT")}'


def funcion_revolver_pwd(pwd:str, public_id:str):
    return public_id[0:5] + pwd[0:2] + public_id[1] + pwd[2::] + public_id

@app.route('/crear', methods=["POST"])
def crear_usuario():
    diccionario : dict = request.json
    correo = diccionario.get("correo")
    # Regex revisar que el correo sea correcto
    # TODO
    try:
        with psycopg2.connect(DSN) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("select * from users where correo = %s", vars=(correo,))
                datos = cur.fetchall()
                datos : list[dict] = [dict(row) for row in datos]
                assert datos == [], f'El usuario {correo} ya existe'

        public_id = uuid.uuid4().urn[9:]       
        pwd = diccionario.get("pwd")
        pwd_interno = funcion_revolver_pwd(pwd, public_id)

        hsh = bcrypt.hashpw(pwd_interno, bcrypt.gensalt(12))
        with psycopg2.connect(DSN) as conn:
            with conn.cursor() as cur:
                sql = '''\
                    insert into users (public_id, correo, hash)
                    values (%s, %s, %s)
                    '''
                cur.execute(sql, vars=(public_id,correo,hsh,))
                assert cur.rowcount == 1, f'No fue posible crear su usuario'
    except AssertionError as e:
        print(str(e))
        return jsonify({
            "msg":str(e)
        }), 404 #Código estándar de HTTP
    except Exception as e:
        print(str(e))
        return jsonify({
            "msg":str(e)
        }), 500
    else:
        return jsonify({
            "msg":f"El usuario {correo} fue creado éxitosamente"
        }), 201
    
@app.route('/verificar', methods=["POST"])
def verificar_usuario():
    diccionario : dict = request.json
    correo = diccionario.get("correo")
    # Regex revisar que el correo sea correcto
    # TODO
    try:
        with psycopg2.connect(DSN) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("select public_id, hash from users where correo = %s", vars=(correo,))
                datos = cur.fetchall()
                assert cur.rowcount == 1, f'Error de sistema'
                datos : list[dict] = [dict(row) for row in datos]
        public_id = datos[0].get("public_id")
        hsh = datos[0].get("hash")
        pwd = diccionario.get("pwd")
        pwd_interna = funcion_revolver_pwd(pwd, public_id)
        assert bcrypt.checkpw(pwd_interna, hsh), f'Contrasenia incorrecta'
    except Exception as e:
        return jsonify({
            "msg":str(e)
        }), 500
    else:
        return jsonify({"msg":"Contrasnia correcta"}), 200

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)



