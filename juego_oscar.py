#%%
import time
import threading
from queue import Queue
from dataclasses import dataclass
import random

Contar:int

def cronometro(tiempo:int):
    second=0
    global Contar

    while True:
     #Se detiene un segundo para realizar el conteo
        time.sleep(1)
        second=second + 1
        print(second)
        print(Contar)
        if second>tiempo:
            Contar=1
            break



#Jugadores
@dataclass
class Jugador:
    puntaje:0
    Turno:int
    tiempo_juego:str

    def Temporizador(self,tiempo:int):
        second=0

        while True:
        #Se detiene un segundo para realizar el conteo
            time.sleep(1)
            second=second + 1
            print(second)
            if second>tiempo:
                self.tiempo_juego='acabado'
                break
 
    def contar_puntos(self):
 
        global puntaje

        while True:
            #Aqui ingresariamos los botones que se pulsaran
            print('jugando')
            print(self.tiempo_juego)
            if self.tiempo_juego == 'acabado':
                break

    def descontar_puntos(self):
 
        global puntaje

        while True:
            #Aqui ingresariamos los botones que se pulsaran
            print('jugando')
            print(self.tiempo_juego)
            if self.tiempo_juego == 'acabado':
                break 

    def jugar(self,tiempo:int):
       
       hilo_temporizador=threading.Thread(target=self.Temporizador,args=(tiempo,))
       hilo_contar=threading.Thread(target=self.contar_puntos)
       hilo_descontar=threading.Thread(target=self.descontar_puntos)

       if self.Turno==1:
          hilo_temporizador.start()
          hilo_contar.start()

          hilo_temporizador.join()
          hilo_contar.join()

          print(self.tiempo_juego)

       if self.Turno==2:
          hilo_temporizador.start()
          hilo_descontar.start()

          hilo_temporizador.join()
          hilo_descontar.join()

          print(self.tiempo_juego)


#Empezamos el juego
variable_jugador = random.randint(1,2)
variable_juego = random.randint(1,8)
Contar=0

Jugador1= Jugador(0,1,'jugar')
Jugador2= Jugador(0,1,'jugar')

hilo_cronometro=threading.Thread(target=cronometro,args=(5,))
hilo_cronometro.start()

while True:
    variable_jugador = random.randint(1,2)
    variable_juego = random.randint(1,8)

    hilo_jugar1= threading.Thread(target=Jugador1.jugar,args=(variable_juego,))
    hilo_jugar2= threading.Thread(target=Jugador2.jugar,args=(variable_juego,))


    if variable_jugador==1:
     
     Jugador1.Turno=1
     Jugador2.Turno=2

     hilo_jugar1.start()
     hilo_jugar2.start()

     hilo_jugar1.join()
     hilo_jugar2.join()

     Jugador1.Turno='jugar'
     Jugador2.Turno='jugar'



    else:
     Jugador1.Turno=2
     Jugador2.Turno=1

     hilo_jugar1.start()
     hilo_jugar2.start()

     hilo_jugar1.join()
     hilo_jugar2.join()
     
     Jugador1.Turno='jugar'
     Jugador2.Turno='jugar'


    if Contar==1:
       break


    






# %%
