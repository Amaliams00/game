import random
from os import system
import time
from pygame import mixer

def generateRandom():
    
    return random.randint(0, 100)
    
# end def

def NavBar():
    print("¡Adivina el número!")
    print("Se encuentra entre 0 y 100")
# end def

def play():
    
    num = generateRandom()
    total_puntos = 0
    fails = 0
    
    while fails < 5:
    
        NavBar()
        
        num_input = int(input("Introduzca un número: "))
        
        if num == num_input:
            total_puntos = total_puntos + 1
            mixer.init()
            mixer.music.load('http://www.sonidosmp3gratis.com/sounds/iphone-notificacion.mp3')
            mixer.music.play()
            print("Acertaste en el número, sumas un punto, total de puntos: " + str(total_puntos))
            fails = 0
            num = generateRandom()
        else :
            print("Fallaste vuelve a intentarlo")
            fails = fails + 1
        # end if
        
        time.sleep(1)
        system("cls")
        
    # end while
    
    print("¡El Juego ha terminado!")
    print("Total de puntos: " + str(total_puntos))
    
# end def

play()
