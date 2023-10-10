from gpiozero import LED, Button
import time
import random
import threading

class Jugador(object):
    def __init__(self, button_io:int, led_io:int, jugador:int, tiempo_restante=30):
        self.button_io = Button(button_io)
        self.led_io = LED(led_io)
        self.tiempo_restante = tiempo_restante
        self.jugador = jugador

        self.conteo = 0

    def __str__(self):
        return f'Jugador-{self.jugador} - Conteo: {self.conteo}'
    
    def __call__(self, *args, **kwargs):
        self.run()

    def click(self):
        self.led_io.on()
        duracion = random.uniform(2, 8)
        start = time.time()
        while duracion > 0 and self.tiempo_restante > 0:
            time.sleep(0.5)
            if self.button_io.is_active:
                self.conteo += 1
                print(f'Jugador {self.jugador} + 1 puntos')
            duracion -= time.time() - start
            self.tiempo_restante -= duracion
        self.led_io.off()
        return

    def pause(self):
        duracion = random.uniform(4, 8)
        start = time.time()
        while duracion > 0 and self.tiempo_restante > 0:
            time.sleep(0.5)
            if self.button_io.is_active:
                self.conteo -= 5
                print(f'Jugador {self.jugador} - 5 puntos')
            duracion -= time.time() - start
            self.tiempo_restante -= duracion
        return
    
    def run(self):
        while self.tiempo_restante > 0:
            print(f'tiempo restante = {self.tiempo_restante}')
            self.click()
            self.pause()
        print(f'Fin del juego. {self}')


jugador1 = threading.Thread(target=Jugador(button_io=14, led_io=15, jugador=1))
jugador2 = threading.Thread(target=Jugador(button_io=23, led_io=24, jugador=2))

jugador1.start()
jugador2.start()
