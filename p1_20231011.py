from gpiozero import LED
import time

R = LED(13)
G = LED(15)
B = LED(16)

entradas = [
    {
        "color":"r",
        "func":R,
    },
    {
        "color":"g",
        "func":G
    },
    {
        "color":"b",
        "func":B
    }
]

color : str = input("Favor de ingresar el color a encender [r,g,b]")
parpadeo : str = input("Favor de especificar si se quiere parpaenado [y/n]")

def correr_led(color:str, parpadeo:str):
    assert color.lower() in ['r', 'g', 'b']
    assert parpadeo.lower() in ['y', 'n']

    myDict  = [fila for fila in entradas if fila.get('color') == color.lower()][0]
    parpadeo = parpadeo.lower() == 'y'

    while True:
        if parpadeo:
            myDict['func'].on()
            time.sleep(0.5)
            myDict['func'].off()
            time.sleep(0.5)
        else:
            myDict['func'].on()





