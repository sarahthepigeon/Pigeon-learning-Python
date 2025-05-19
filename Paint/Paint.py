import sys
import pygame
import time
from pygame.locals import *

#initalize the game
pygame.init()

# strokes = [stroke1, stroke2, stroke3]
# stroke1 = [(0, 0), (100, 100), (200, 200), ...]
strokes = []

# set background parameters
size = width, height = 800, 600
bg_color = (0, 0 ,0)
screen = pygame.display.set_mode(size)
screen.fill(bg_color)

# clock
clock = pygame.time.Clock()

drawing = 0

mouse_pos = pygame.mouse.get_pos()
last_mouse_pos = mouse_pos

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_RETURN:
                # print the stroke
                for idx, stroke in enumerate(strokes, 1):
                    print(f"Stroke {idx}: {stroke}")
            if event.key == K_p:
                # redraw the stroke with a different color
                pass

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = 1
                last_mouse_pos = event.pos
                # create a new stroke
                strokes.append([])
                strokes[-1].append(event.pos)

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = 0

        if event.type == MOUSEMOTION and drawing == 1:
            mouse_pos = event.pos
            pygame.draw.line(screen, (255, 255, 255), last_mouse_pos, mouse_pos,5)
            # update mouse position
            last_mouse_pos = mouse_pos
            # update stroke
            strokes[-1].append(mouse_pos)

    # double buffer flip
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)