import random
from os import system
import time
from pygame import mixer
import pygame

pygame.init()
size= (600, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

letra = pygame.font.SysFont("Arial", 30)
header = pygame.font.SysFont("Arial", 60)
footer = pygame.font.SysFont("Arial", 20)

jugador = ""
puntos = 0

def DrawHeader():
    headerTxt = header.render("Adivina el Numero!" ,True, (255,255,255), (0,0,0))  
    screen.blit(headerTxt, (100,50))
    pygame.display.flip()
    headerTxt = footer.render("Se encuentra entre 0 y 100" ,True, (255,255,255), (0,0,0))  
    screen.blit(headerTxt, (200,130))
    pygame.display.flip()
#end-def

def DrawFooter():
    footerTxt = footer.render("Presiona Espacio para continuar." ,True, (255,255,255), (0,0,0))  
    screen.blit(footerTxt, (150,400))
    pygame.display.flip()  
#end-def

def DrawMidSection():
    midTxt = letra.render("Numero: " ,True, (255,255,255), (0,0,0))  
    screen.blit(midTxt, (200,300))
    pygame.display.flip()
    midTxt2 = letra.render("Puntos: " + str(puntos),True, (255,255,255), (0,0,0))  
    screen.blit(midTxt2, (200,200))
    pygame.display.flip() 
#end-def

def DrawScreen():
    screen.fill((0,0,0))
    DrawHeader()
    DrawMidSection()
    DrawFooter()
#end-def

def generateRandom():
    return random.randint(0, 100)
#end-def
         
num = generateRandom()
print(num)

isCheck = False


DrawScreen()

cant_escrita = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((0,0,0))
                if jugador != "":
                    if int(jugador) ==  num:
                        result = "Ganaste!"
                        puntos = puntos + 1
                        num = generateRandom() 
                        print(num)
                        mixer.init()
                        mixer.music.load('iphone-notificacion (1).mp3')
                        mixer.music.play()
                    else:
                        result = "Fallaste!"
                    #end-if
                #end-if
                GameOverTxt = header.render(result,True, (255,255,255), (0,0,0))  
                screen.blit(GameOverTxt, (200,200))
                pygame.display.flip()
                DrawFooter()
                done2 = False
                while not done2:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:
                            done2 = True
                        elif event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_SPACE:
                                done2 = True
                            #end-if
                        #end-if
                    #end-for
                #end-while
                DrawScreen()
                cant_escrita = 0
                jugador = ""
            else:
                if cant_escrita < 3:
                    imagenTxt = letra.render(event.unicode, True, (255,255,255), (0,0,0))
                    screen.blit(imagenTxt, (330 + cant_escrita*15,300))
                    pygame.display.flip()
                    jugador = jugador + event.unicode
                    print(jugador)
                    cant_escrita = cant_escrita + 1
                #end-if
            #end-if
        #end-iff
    #end-for
#end-while