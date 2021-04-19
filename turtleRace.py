import pygame
import sys
import random


pygame.init()

class Runner():
    __customes = ("turtle", "fish", "moray", "octopus", "prawn") #Estos son los disfraces de todos los corredores, a partir del nuevo atrbuto creado "customes" 
    
    def __init__(self, x=0, y=0): #En esta linea se crea al corredor y se le posiciona en la coordenada que se desee
        
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) # Custome es "disfraz", para la  crecion de personajes
        self.position = [x, y] #Se asignará su posición de salida e la funcion competir. Es mutable, tiene que ser una lista, por eso va entre corchetes.
        self.name = ""
        
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        
        
class Game():
    runners = [] #Atributo de la clase Game, una lista de los corredores
    __posY = (150, 195, 240, 285)
    __names = ("Speedy", "Lucera", "Alonso", "Torcuato")
    __startLine = -5
    __finishLine = 620
    
   
    def __init__(self):
       self.__screen = pygame.display.set_mode((640, 480))
       self.__background = pygame.image.load("images/background.png")
       pygame.display.set_caption("Carrera de bichos")
        
       for i in range(4):
           
           theRunner = Runner(self.__startLine, self.__posY[i]) #Esto es una instancia del objeto Runner en la posicion 0,0 de la pantalla
           theRunner.name = self.__names[i]
           self.runners.append(theRunner)
       
    
    
    def close(self):
        pygame.quit()
        sys.exit()
    
    def competir(self):
        gameOver = False

#COMPROBAR EVENTOS:
        while not gameOver:
            for event in pygame.event.get(): #Este es el buffer donde pygame va almacenando los venetos que suceden en pnatalla
                if event.type == pygame.quit: #Este es el evento mas basico de pygame, que es cerrar la pantalla
                    gameOver = True

#ACTAULIZAR EVENTOS:           
            for activeRunner in self.runners: #La variable activeRunner solo existe en el ambito de la funin competir. En este caso self.runners es una lista
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))#Las variables que llevan el self forman parte de la clase y estan presentes en todo el codigo
                    gameOver = True
                

#REFRESCAR LA PANTALLA:
            self.__screen.blit(self.__background, (0,0)) #Atributo de Game. Esta linea equivale a la parte del ciclo que es actualizar la pantalla
            

            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()  #Esta linea sirve para refrescar la pantalla
 
 
 
        while True: #Este bucle lo que hace es comprobar los eventos una vez se ha salido del anterior bucle while, que ya ha dictaminado el gameOver
                    #y cierra el objeto Game para que no siga llenandose el buffer
            for event in pygame.event.get(): #Este get va limpiando los eventos que suceden, por ejemplo que pase el raton por la pantalla, pero como no interactua con el codigo, no guarda esos eventos y no se llena 
                if event.type == pygame.quit:
                    pygame.quit()
                    sys.exit()
                    
    
        
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()