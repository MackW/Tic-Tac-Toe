import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class TTTMain:
    """The Main Tic-Tac-Toe Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(500, 30)
        
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.DrawBoard(self.screen)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.KeyPressed(event.key)

                            
                            
            pygame.display.flip()
    def DrawBoard(self,screen):
        pygame.draw.lines(screen, (255, 255, 255), False, [(238,80), (238,420)], 4)
        pygame.draw.lines(screen, (255, 255, 255), False, [(398,80), (398,420)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,178), (560,178)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,298), (560,298)], 4)    
                                 
    def KeyPressed(self,key):
        font = pygame.font.Font(None, 36)
        text = font.render("X", 1, (255, 0, 0))
        if (key == K_1):
            textpos = text.get_rect(centerx=160,centery=120)
        elif (key == K_2):
            textpos = text.get_rect(centerx=320,centery=120)
        elif (key == K_3):
            textpos = text.get_rect(centerx=480,centery=120)
        elif (key == K_4):
            textpos = text.get_rect(centerx=160,centery=240)
        elif (key == K_5):
            textpos = text.get_rect(centerx=320,centery=240)
        elif (key == K_6):
            textpos = text.get_rect(centerx=480,centery=240)
        elif (key == K_7): 
            textpos = text.get_rect(centerx=160,centery=360)                       
        elif (key == K_8):
            textpos = text.get_rect(centerx=320,centery=360)
        elif (key == K_9):
            textpos = text.get_rect(centerx=480,centery=360)
        self.screen.blit(text, textpos)      
    
                    
if __name__ == "__main__":
    MainWindow = TTTMain()
    MainWindow.MainLoop()