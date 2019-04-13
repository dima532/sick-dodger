import sys,pygame
import time
from mouseshot import mouseshoot as ms
import random as r
pygame.init()
(width, height) = (935, 438)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sick dodger")
class bullet():#класс для пули
    def __init__(self, x, y, c):
        self.x=x
        self.y=y
        self.speed = 5
        self.walkcount=0
        self.isexist= False

    def draw(self, screen):
        if self.walkcount + 1 >= 20:
            self.walkcount=0
        screen.blit(bull[self.walkcount//5],(self.x,self.y) )
        self.walkcount+=1
