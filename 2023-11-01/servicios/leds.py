from gpiozero import LED

diccionario : dict[int, LED] = {
    1:LED(14),
    2:LED(18),
    3:LED(20)
}

def status(led_id:int) -> bool:
    return diccionario[led_id].is_active

def regresa_todos_status() -> list[dict]:
    resultados = list()
    for llave in diccionario.keys():
        _id = llave
        _status = status(llave)
        resultados.append({'id':_id, 'status':_status})
    return resultados

def click(led_id:int) -> None:
    led = diccionario[led_id]
    if led.is_active: 
        led.off()
    else:
        led.on()
