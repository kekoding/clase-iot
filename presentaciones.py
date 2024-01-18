import random

equipos = [
    {1:"Coacalco"},
    {2:"Dinamita"},
    {3:"JIMB"},
    {4:"RaspPerros"},
    {5:"ETL"},
    {6:"Bits Forgers"}
]

orden_equipos : list[int] = []
i = 0

while len(orden_equipos) < len(equipos):
    if i < 100:
        i += 1
        continue
    nuevo_num = random.randint(1, len(equipos))
    if nuevo_num in orden_equipos: continue
    orden_equipos.append(nuevo_num)

for orden in orden_equipos:
    print(equipos[orden-1])