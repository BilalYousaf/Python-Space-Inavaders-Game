import pygame
class InvaderMissile:
        invaderMissileImg=None
        @staticmethod
        def setImg():
                InvaderMissile.invaderMissileImg = pygame.image.load(
                        'invadermissileimg.png')
        def __init__(self, xInitialPos, yInitialPos):
                self.__missilePosX = xInitialPos
                self.__missilePosY = yInitialPos

        def move(self):
                self.__missilePosY = self.__missilePosY + 4

        def draw (self, screen):
                screen.blit(self.Invadermissile.Img,(self.__missilePosX,self.__missilePosY)) 

        
    
