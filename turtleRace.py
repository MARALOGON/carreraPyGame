import pygame
import sys

pygame.init()

class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
       self.__screen = pygame.display.set_mode((640, 480))
       self.__background = pygame.image.load("images/background.png")
       pygame.display.set_caption("Carrera de bichos")


    def competir(self):
        gameOver = False

        while True:
            for event in pygame.event.get(): #Este es el buffer donde pygame va almacenando los venetos que suceden en pnatalla
                if event.type == pygame.quit: #Este es el evento mas basico de pygame, que es cerrar la pantalla
                    gameOver = True

            self.__screen.blit(self.__background, (0,0)) #Esta linea equivale a la parte del ciclo que es actualizar la pantalla
            
            pygame.display.flip()  #Esta linea sirve para refrescar la pantalla
            
        
        pygame.quit()
        sys.exit()
        
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()