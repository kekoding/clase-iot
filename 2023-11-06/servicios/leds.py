import time
from gpiozero import LED

def click_led(led:LED) -> None:
    '''Sí el led está encendido, entonces lo apagado. Si está
    apagado, enciende el LED

    Parametros:
        led_pintout:int - Pinout en donde está conectado el led

    Regresa:
        None
    '''
    print(f"led esta activo = {led.is_active}")
    if led.is_active:
        led.off()
    else:
        led.on()
    return
