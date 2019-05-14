import sys,pygame
import time
pygame.init()
(width, height) = (935, 438)
screen = pygame.display.set_mode((width, height))

def mouseshoot():
    pygame.mouse.get_pos()[0]
    pygame.mouse.get_pressed()[0]
