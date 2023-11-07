from gpiozero import LED

def click_led(led:LED) -> None:
    if led.is_active:
        led.off()
        msg = f'El led {led.pin} se apagó'
    else:
        led.on()
        msg = f'El led {led.pin} se encendió'
    return msg
