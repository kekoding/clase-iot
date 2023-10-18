# %%

nombres = ['Alejandra', 'Roberto']

with open('./nuevos_nombres.txt', mode='w') as f:
    for nombre in nombres:
        f.writelines(f'El nombre es: {nombre}\n')



['Alejandra    26    Saltillo\n', 'Jaime        42    Mazatlan\n']

'''
La librería open tiene 3 modos
"r" - read
"w" - write - escribe un nuevo archivo
"a" - append - (anexar), anexar información del archivo
'''
# %%
