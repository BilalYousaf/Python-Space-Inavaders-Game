import sys
import pygame
import Invader
#import InvaderMissile
import Missile
from pygame.locals import *

class SpaceInvader:

    # Constructor of the basic game class.
    # This constructor calls initialize and main_loop method.
    def __init__(self):
        self.initialize()
        self.main_loop()

    # Initialization method. Allows the game to initialize different
    # parameters and load assets before the game runs
    def initialize(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)

        self.width = 1024
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.caption = "Space Invader!!"
        pygame.display.set_caption(self.caption)

        self.rocketXPos = 512
        self.alienXPos = 512
        self.alienYPos = 340
        
        self.framerate = 60

        self.clock = pygame.time.Clock()

       # self.gameState = 1
        #self.initializeGameVariables ()
        
        
       # def initializeGameVariab
        self.backgroundImg = pygame.image.load('Starfield1024x768.PNG')
        self.rocketLauncherImg = pygame.image.load('1448318577_kspaceduel.png')
        self.invaderImg = pygame.image.load('invaders2.png')
        self.missileImg = pygame.image.load('bullets.png')
        #self.invadernissileImg =pygame.image.load('bullets.png')
        #InvaderMissile.InvaderMissile.setImg()

        self.rocketXPos = 512
        #self.alienXPos = 512
        #self.alienYPos = 100
        
        self.alienDirection = -1
        self.alienSpeed = 16
        self.ticks = 0
        self.invaders = []
        xPos =512
        
        for i in range (11):
            invader = Invader.Invader()
            invader.setPosX (xPos)
            invader.setPosY (100)
            self.invaders.append(invader)
            xPos += 30
        self.missileFired = None
            
            

        self.missileXPos =  -1
        self.missileYPos=  -1
        

        self.missileFired = None 
        


    # main loop method keeps the game running. This method continuously
    # calls the update and draw methods to keep the game alive.

    def main_loop(self):
        self.clock = pygame.time.Clock()
        while True:
            gametime = self.clock.get_time()
            self.update(gametime)
            self.draw(gametime)
            self.clock.tick(self.framerate)
            
    # Update method contains game update logic, such as updating the game
    # variables, checking for collisions, gathering input, and
    # playing audio.
    
    def update(self, gametime):        
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rocketXPos = self.rocketXPos + 5
                elif event.key == pygame.K_LEFT:
                    self.rocketXPos = self.rocketXPos - 5
                elif event.key == pygame.K_SPACE:
                    self.missileFired = Missile.Missile(self.rocketXPos, 650)
            invaderFound = False
            for i in range (11):
                if self.invaders [i] != None:
                    invaderFound = True
                    break
            if invaderFound == False:
                pygame.quit ()
                sys.exit ()
                
                    



        if (self.missileFired != None):
            self.missileFired.move()

        
                    
                    # elif event.key == pygame.K_SPACE and self.missileFired == False:
                    #self.missileXPos = self.rocketXPos
                    #self.missileYPos = 650 - self.missileImg.get_height()
                   # self.missileFired = True
                    
        #if self.missileFired == True:
          #self.missileYPos = self.missileYPos - 1

      #  if self.missileYPos < 100:
         #   self.missileFired = False 

        if self.rocketXPos < 100:
            self.rocketXPos = 100
                
        if self.rocketXPos > 924:
            self.rocketXPos = 924
                
        self.ticks = self.ticks +gametime
        if self.ticks >500:
            for i in range (11):
                if self.invaders [i] != None:
                    self.invaders[i].moveHorizontal(self.alienSpeed * self.alienDirection)

            leftMostInvader = None
            rightMostInvader = None

            for i in range (11):
                 if self.invaders[i] != None:
                      leftMostInvader = self.invaders[i]
                      break
            for i in range (10, -1, -1):
                if self.invaders[i] != None:
                     rightMostInvader = self.invaders [i]
                     break
                        
                self.invaders[i].moveHorizontal(self.alienSpeed * self.alienDirection)

            if self.invaders[0].getPosX() < 96:
                self.alienDirection = +1

                xPos = 96
                for i in range(11):
                    if self.invaders[i] != None:
                        self.invaders [i].moveVertical(4)
                        self.invaders[i].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width ()
                    #xPos = xPos + 30

            if self.invaders[10].getPosX() > 924:
                self.alienDirection = -1

                xPos = 924 - self.invaderImg.get_width() * 10
                for i in range(11):
                    if self.invaders[i] != None:
                        self.invaders[i].moveVertical(4)
                        self.invaders[i].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width ()
                    #xPos = xPos + 30
                    
            self.ticks = 0

            
        if self.missileFired != None:
            rectMissile = pygame.Rect(self.missileFired.getPosX(), self.missileFired.getPosY(), self.missileImg.get_width(), self.missileImg.get_height())
            for i in range(11):
                if self.invaders[i] != None:
                    rectInvader = pygame.Rect(self.invaders[i].getPosX(), self.invaders[i].getPosY(), self.invaderImg.get_width(), self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders[i] = None
                        break

                                                                                        
                                                                                        
                       
      #  self.alienXPos = self.alienXPos + 1 * self.alienDirection
        #if self.alienXPos < 100:
            #self.alienXPos = 100
            #self.alienDirection =  +1
            #self.alienYPos = self.alienYPos + 12
            
        #if self.alienXPos > 924:
            #self.alienXPos = 924
            #self.alienDirection = -1
            #self.alienYPos = self.alienYPos + 12
        #if self.alienYPos > 350:
            #self.alienspeed = 2
              
            
            
            
                              
    # Draw method, draws the current state of the game on the screen                        
    def draw(self, gametime):              
        self.screen.blit(self.backgroundImg, (0,0))
        self.screen.blit(self.rocketLauncherImg, (self.rocketXPos, 650))
        
        if self.missileFired != None:
            self.screen.blit(self.missileImg, (self.missileFired.getPosX(),self.missileFired.getPosY() - self.missileImg.get_height()))
            #self.screen.blit(self.missileImg, self.missileFired.getPosition())


        for i in range (11):
           if self.invaders [i] != None:
                self.screen.blit(self.invaderImg,self.invaders[i].getPosition())

                             
        #self.screen.blit(self.invaderImg, (self.alienXPos, self.alienYPos))
        #if self.missileFired == True:
           # self.screen.blit(self.missileImg, (self.missileXPos,self.missileYPos))
                                                        
        pygame.display.flip()    


if __name__ == "__main__":
    game = SpaceInvader()
