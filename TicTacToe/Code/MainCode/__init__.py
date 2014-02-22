import os, sys,random
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class TTTMain:
    """The Main Tic-Tac-Toe Class - This class handles the main 
    initialization and creating of the Game."""
    Board =[0,0,0,0,0,0,0,0,0]
    Playing = "X"
    level=1
    whoStarts="X"
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
        
        self.screen.fill((0,0,0))
        self.DrawBoard(self.screen)
        for x in xrange(0, 9):
            self.DrawPosition(x, str(x+1), (64, 64, 64),0)
           
        while 1:
            self.IntroScreen()     
            self.PlayGame()
            self.WaitForKeyAndResetGame()

    def WaitForKeyAndResetGame(self):
        exitloop = 0
        font = pygame.font.Font(None, 72)                                                                                        
        text = font.render("Press Any Key", 1, (0, 255, 0))                               
        textpos = text.get_rect(centerx=self.width/2,centery=278)
        self.screen.blit(text, textpos) 
        pygame.display.flip()
        while exitloop == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    exitloop=1
                               
    def IntroScreen(self):
        exitloop = 0
        self.UpdateIntroText()
        while exitloop == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key==K_1:
                        self.whoStarts="X"
                        self.UpdateIntroText()
                    elif event.key==K_2:
                        self.whoStarts="O"
                        self.UpdateIntroText()                        
                    elif event.key==K_x:
                        self.Playing="X"
                        self.UpdateIntroText()                    
                    elif event.key==K_o:
                        self.Playing="O"
                        self.UpdateIntroText()                    
                    elif event.key==K_SPACE:
                        exitloop=1       
        self.screen.fill((0,0,0)) 
        pygame.display.flip()
        self.DrawBoard(self.screen)
        for x in xrange(0, 9):
            self.DrawPosition(x, str(x+1), (64, 64, 64),0)   
        self.Board =[0,0,0,0,0,0,0,0,0]
        font = pygame.font.Font(None, 36)                                                                                        
        text = font.render("You Are Playing : "+ self.Playing, 1, (0, 255, 0))                               
        textpos = text.get_rect(centerx=self.width/2,centery=440)
        self.screen.blit(text, textpos) 
        pygame.display.flip()
     
    def UpdateIntroText(self):    
        self.screen.fill((0,0,0)) 
        pygame.display.flip() 
        font = pygame.font.Font(None, 48)    
        text = font.render("Playing (X or O to change) : " + self.Playing, 1, (0, 255, 0))                               
        textpos = text.get_rect(centerx=self.width/2,centery=80)
        self.screen.blit(text, textpos) 
        text = font.render("Who Starts (1 or 2 to change) : " + self.whoStarts, 1, (0, 255, 0))                               
        textpos = text.get_rect(centerx=self.width/2,centery=160)
        self.screen.blit(text, textpos)                                                                                     
        text = font.render("Press Space to Start", 1, (0, 255, 0))                               
        textpos = text.get_rect(centerx=self.width/2,centery=self.height/2)
        self.screen.blit(text, textpos) 
        pygame.display.flip()
    def PlayGame(self):
        exitloop = 0
        if self.Playing!=self.whoStarts:
            self.PlayComputerMove()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN and self.CheckForWin()==0:
                    if self.KeyPressed(event.key) == 1:
                        if self.CheckForWin() ==0:
                            self.PlayComputerMove()
                        if self.CheckForWin()>0:                             
                            msg="You Win" if self.CheckForWin()==self.Playing else "It's A Draw" if self.CheckForWin()==3 else "I Win"    
                            font = pygame.font.Font(None, 72)                                                                                        
                            text = font.render(msg, 1, (0, 255, 0))                               
                            textpos = text.get_rect(centerx=self.width/2,centery=158)
                            self.screen.blit(text, textpos)  
                            exitloop=1                
                pygame.display.flip()
            if exitloop==1:
                break
            
    def DrawBoard(self,screen):
        pygame.draw.lines(screen, (255, 255, 255), False, [(238,80), (238,420)], 4)
        pygame.draw.lines(screen, (255, 255, 255), False, [(398,80), (398,420)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,178), (560,178)], 4)  
        pygame.draw.lines(screen, (255, 255, 255), False, [(80,298), (560,298)], 4)    
                                 
    def KeyPressed(self,key):
        ValidMove=0
        if (key == K_1) and (self.Board[0]==0):
            ValidMove=self.MakeMove(0,self.Playing)
        elif (key == K_2)and (self.Board[1]==0):
            ValidMove=self.MakeMove(1,self.Playing)
        elif (key == K_3)and (self.Board[2]==0):
            ValidMove=self.MakeMove(2,self.Playing)
        elif (key == K_4)and (self.Board[3]==0):
            ValidMove=self.MakeMove(3,self.Playing)
        elif (key == K_5)and (self.Board[4]==0):
            ValidMove=self.MakeMove(4,self.Playing)
        elif (key == K_6)and (self.Board[5]==0):
            ValidMove=self.MakeMove(5,self.Playing)
        elif (key == K_7)and (self.Board[6]==0): 
            ValidMove=self.MakeMove(6,self.Playing)                
        elif (key == K_8)and (self.Board[7]==0):
            ValidMove=self.MakeMove(7,self.Playing)
        elif (key == K_9)and (self.Board[8]==0):
            ValidMove=self.MakeMove(8,self.Playing)
        return ValidMove         
    def MakeMove(self,position,piece):
        self.DrawPosition(position, str(position+1), (0, 0, 0),0)
        self.DrawPosition(position, piece, (255, 0, 0),1)
        self.Board[position]=piece
        self.ValidMove=1
        return 1
        
    def DrawPosition(self,position,piece,colour,ismove):
        font = pygame.font.Font(None, 36)
        text = font.render(piece, 1,colour)
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
        self.screen.blit(text, textpos)  
        
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
    def CheckForLine (self,pos1,pos2,pos3,imPlaying):
        
        pos=-1
        if ((self.Board[pos1]==self.Board[pos2]==imPlaying) and (self.Board[pos3]==0)):
            pos=pos3
        elif ((self.Board[pos2]==self.Board[pos3]==imPlaying) and (self.Board[pos1]==0)):
            pos=pos1
        elif ((self.Board[pos1]==self.Board[pos3]==imPlaying) and (self.Board[pos2]==0)):
            pos=pos2    
        return pos   
    def PlayComputerMove(self):
        playedMove=0
        imPlaying="X" if self.Playing=="O" else "O"
        while playedMove==0 and (self.Board[0]==0 or self.Board[1]==0 or self.Board[2]==0 or self.Board[3]==0 or self.Board[4]==0 
                              or self.Board[5]==0 or self.Board[6]==0 or self.Board[7]==0 or self.Board[8]==0):
            pos=-1
            pos=self.CheckForLine(0, 1, 2,imPlaying)
            if pos==-1: pos=self.CheckForLine(3, 4, 5,imPlaying)
            if pos==-1: pos=self.CheckForLine(6, 7, 8,imPlaying)
            if pos==-1: pos=self.CheckForLine(0, 4, 8,imPlaying)  
            if pos==-1: pos=self.CheckForLine(2, 4, 6,imPlaying)       
            if pos==-1: pos=self.CheckForLine(0, 3, 6,imPlaying)
            if pos==-1: pos=self.CheckForLine(1, 4, 7,imPlaying)
            if pos==-1: pos=self.CheckForLine(2, 5, 8,imPlaying)  
            if pos==-1: pos=self.CheckForLine(0, 1, 2,self.Playing)
            if pos==-1: pos=self.CheckForLine(3, 4, 5,self.Playing)
            if pos==-1: pos=self.CheckForLine(6, 7, 8,self.Playing)
            if pos==-1: pos=self.CheckForLine(0, 4, 8,self.Playing)  
            if pos==-1: pos=self.CheckForLine(2, 4, 6,self.Playing) 
            if pos==-1: pos=self.CheckForLine(0, 3, 6,self.Playing)
            if pos==-1: pos=self.CheckForLine(1, 4, 7,self.Playing)
            if pos==-1: pos=self.CheckForLine(2, 5, 8,self.Playing)
            if pos==-1: pos = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            if self.Board[pos]==0:
                self.Board[pos]=imPlaying
                playedMove =self.MakeMove(pos, self.Board[pos])
        return playedMove    
                    
if __name__ == "__main__":
    MainWindow = TTTMain()
    MainWindow.MainLoop()