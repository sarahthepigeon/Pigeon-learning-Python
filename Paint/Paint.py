import sys
import pygame
import time
from pygame.locals import *

#initalize the game
pygame.init()

# set background parameters
size = width, height = 800, 600
bg = (0, 0 ,0)
screen = pygame.display.set_mode(size)
screen.fill(bg)
drawing_screen = screen.copy()

drawing = 0

mouse_pos = pygame.mouse.get_pos()
last_mouse_pos = mouse_pos

while True:
    screen.blit(drawing_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = 1
                last_mouse_pos = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = 0
                last_mouse_pos = pygame.mouse.get_pos()

    # draw the cursor

    if drawing == 1:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(drawing_screen, (255, 255, 255), last_mouse_pos, mouse_pos,5)
        # update mouse position
        last_mouse_pos = mouse_pos

    # double buffer flip
    pygame.display.flip()
    time.sleep(1/60)