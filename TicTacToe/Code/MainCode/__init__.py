import os, sys,random
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class TTTMain:
    """The Main Tic-Tac-Toe Class - This class handles the main 
    initialization and creating of the Game."""
    Board =[0,0,0,0,0,0,0,0,0]
    Playing = 1 
    """ Defaulting to X"""
    def __init__(self, width=640,height=480):
        """Initialize"""
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
                elif event.type == KEYDOWN and self.CheckForWin()==0:
                    if self.KeyPressed(event.key) == 1:
                        if self.CheckForWin() ==0:
                            self.PlayComputerMove()
                        if self.CheckForWin()>0:                             
                            msg="You Win" if self.CheckForWin()==1 else "It's A Draw" if self.CheckForWin()==3 else "I Win"   
                            font = pygame.font.Font(None, 72)                                                                                        
                            text = font.render(msg, 1, (0, 255, 0))                               
                            textpos = text.get_rect(centerx=self.width/2,centery=self.height/2)
                            self.screen.blit(text, textpos)                  
            pygame.display.flip()
            
    def DrawBoard(self,screen):
        pygame.draw.lines(screen, (255, 255, 255), False, [(238,80), (238,420)], 4)
        pygame.draw.lines(screen, (255, 255, 255), False, [(398,80), (398,420)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,178), (560,178)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,298), (560,298)], 4)    
                                 
    def KeyPressed(self,key):
        ValidMove=0
        if (key == K_1) and (self.Board[0]==0):
            ValidMove=self.DrawPosition(0, self.Playing)
        elif (key == K_2)and (self.Board[1]==0):
            ValidMove=self.DrawPosition(1, self.Playing)
        elif (key == K_3)and (self.Board[2]==0):
            ValidMove=self.DrawPosition(2, self.Playing)
        elif (key == K_4)and (self.Board[3]==0):
            ValidMove=self.DrawPosition(3, self.Playing)
        elif (key == K_5)and (self.Board[4]==0):
            ValidMove=self.DrawPosition(4, self.Playing)
        elif (key == K_6)and (self.Board[5]==0):
            ValidMove=self.DrawPosition(5, self.Playing)
        elif (key == K_7)and (self.Board[6]==0): 
            ValidMove=self.DrawPosition(6, self.Playing)                     
        elif (key == K_8)and (self.Board[7]==0):
            ValidMove=self.DrawPosition(7, self.Playing)
        elif (key == K_9)and (self.Board[8]==0):
            ValidMove=self.DrawPosition(8, self.Playing)
        return ValidMove         
    
    def DrawPosition(self,position,piece):
        font = pygame.font.Font(None, 36)
        text = font.render("X" if piece==1 else "O", 1, (255, 0, 0))
        if (position==0):
            textpos = text.get_rect(centerx=160,centery=120)      
        elif (position==1):
            textpos = text.get_rect(centerx=320,centery=120)
        elif (position==2):
            textpos = text.get_rect(centerx=480,centery=120)
        elif (position==3):
            textpos = text.get_rect(centerx=160,centery=240)
        elif (position==4):
            textpos = text.get_rect(centerx=320,centery=240)
        elif (position==5):
            textpos = text.get_rect(centerx=480,centery=240)
        elif (position==6):
            textpos = text.get_rect(centerx=160,centery=360)                      
        elif (position==7):
            textpos = text.get_rect(centerx=320,centery=360)
        elif (position==8):
            textpos = text.get_rect(centerx=480,centery=360)
        self.ValidMove=1
        self.Board[position]=piece
        self.screen.blit(text, textpos)  
        return 1
        
    def CheckForWin(self):
        win =0
        if (self.Board[0]==self.Board[1]==self.Board[2]):
            win=self.Board[0]
        elif (self.Board[3]==self.Board[4]==self.Board[5]):
            win=self.Board[3]
        elif (self.Board[6]==self.Board[7]==self.Board[8]):
            win=self.Board[6]
        elif (self.Board[0]==self.Board[3]==self.Board[6]):
            win=self.Board[0]
        elif (self.Board[1]==self.Board[4]==self.Board[7]):
            win=self.Board[1]
        elif (self.Board[2]==self.Board[5]==self.Board[8]):
            win=self.Board[2]
        elif (self.Board[0]==self.Board[4]==self.Board[8]):
            win=self.Board[0]
        elif (self.Board[2]==self.Board[4]==self.Board[6]):
            win=self.Board[2]
        elif (self.Board[0]>0 and self.Board[1]>0 and self.Board[2]>0 and self.Board[3]>0 and self.Board[4]>0 
                              and self.Board[5]>0 and self.Board[6]>0 and self.Board[7]>0 and self.Board[8]>0):
            win=3                                                            
        return win
    
    def PlayComputerMove(self):
        playedMove=0
        while playedMove==0 and (self.Board[0]==0 or self.Board[1]==0 or self.Board[2]==0 or self.Board[3]==0 or self.Board[4]==0 
                              or self.Board[5]==0 or self.Board[6]==0 or self.Board[7]==0 or self.Board[8]==0):
            pos = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            if self.Board[pos]==0:
                self.Board[pos]=1 if self.Playing==1 else 2
                playedMove =self.DrawPosition(pos, 1 if self.Playing==2 else 2)
        return playedMove    
                    
if __name__ == "__main__":
    MainWindow = TTTMain()
    MainWindow.MainLoop()