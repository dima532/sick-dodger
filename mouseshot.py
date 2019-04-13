import sys,pygame
import time
pygame.init()
(width, height) = (935, 438)
screen = pygame.display.set_mode((width, height))

def mouseshoot():
    pygame.init()
    pygame.display.set_mode((300,200))
    pygame.display.set_caption('Testing')
    running = True
    while running:
        print (pygame.mouse.get_pos()[0])
