class Invader:
    def __init__(self): #__ makes it private
        self.__alienPosX = 0
        self.__alienPosY = 0

    def setPosX (self, x):
        self.__alienPosX = x

    def setPosY (self, Y):
        self.__slienPosY = x

    def getPosX (self):
        return self.__alienPosX
    
    def getPosY (self):
        return self.__alienPosY

    def getPosition(self):
        return (self.__alienPosX, self.__alienPosY)

    def moveHorizontal (self, amount):
        self.__alienPosX = self.__alienPosX + amount

    def moveVertical (Self, amount):
        self.__alienPosY = self.__alienPosY + amount
        
        
