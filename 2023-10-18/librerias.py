'''
Recursos
https://docs.python.org/es/3.10/library/datetime.html

astimezone - Localizar una fecha a la zona horaria que yo le indiqué
Si quiero cambiar una zona horario, utilizar la función replace

3 Blue - 1 Brown
https://www.youtube.com/watch?v=aircAruvnKk

'''

""""
Ejemplo de String de Zona Horaria iso8601

2023-10-18T18:34:05.045Z"""




# %%
import datetime


mi_fechatiempo = datetime.datetime.now(datetime.timezone.utc).isoformat()

mi_fecha = mi_fechatiempo.date()
mi_fecha_str = mi_fechatiempo.strftime('%Y-%m-%d')
#%%

otra_fecha = datetime.datetime.strptime('2023-10-19 17:06:00', '%Y-%m-%d %H:%M:%S').date()
print(otra_fecha)

fecha_iso = datetime.datetime.fromisoformat("2021-01-01T00:00:00.000Z")


# %%
import pytz

fecha_utc = datetime.datetime.now(datetime.timezone.utc)
fecha_local = fecha_utc.replace(tzinfo=pytz.timezone("America/Monterrey"))

print(fecha_utc)
print(fecha_local)




# %%
import pandas as pd


mi_table = pd.DataFrame([
    {'a': 1, 'b': 4, 'c': 'x'},
    {'a': 1, 'b': 4, 'c': 'x'},
    {'a': 3, 'b': 6, 'c': 'y'}
])

mi_table["a"] = mi_table["a"] * 2
# %%
import pandas as pd

df = pd.read_csv('../2023-10-16/datos.csv')

# df.rename(columns={'Temperatura':'temperatura'}, inplace=True)


for column in df.columns:
    c = str.lower(column).strip()
    df[column] = df[column].astype()

import requests





# %%
