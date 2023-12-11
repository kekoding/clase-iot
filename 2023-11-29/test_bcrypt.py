import bcrypt

password = '12345'

# El '12' que determina la velocidad (complejidad) de la sal generada
bcrypt.hashpw(password, bcrypt.gensalt( 12 ))

def get_hashed_password(plain_text_password):
    # Aplicar un hash a la contraseña
    # La sal es alamacenada en la contraseña
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    # Revisar el hash y comparar contra la contraseña real
    return bcrypt.checkpw(plain_text_password, hashed_password)