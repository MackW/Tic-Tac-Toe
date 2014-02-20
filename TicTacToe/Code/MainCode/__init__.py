import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PyManMain:
    """The Main PyMan Class - This class handles the main 
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
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_1)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                            self.KeyPressed(event.key)
                            
            pygame.display.flip()
                            
    def KeyPressed(self,key):
        font = pygame.font.Font(None, 36)
        text = font.render("X", 1, (255, 0, 0))
        if (key == K_1):
            textpos = text.get_rect(centerx=self.width/2,centery=self.height/2)
        elif (key == K_2):   
            textpos = text.get_rect(centerx=self.width/2)
        self.screen.blit(text, textpos)      
                    
if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()