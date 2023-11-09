import requests

datos = requests.get(url='https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m')


## Prueba de Agregar body
login_data =  {
    "usuario":"jorge",
    "contrasenia":"jorge123"
}
respuesta = requests.post("http://localhost:4444/login", data=login_data)
assert respuesta.status_code == 200, f'Error: {respuesta.content}'
