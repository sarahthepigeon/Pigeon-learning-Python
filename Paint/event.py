import sys
from wsgiref.validate import check_iterator

import pygame

pygame.init()

size = width, height = 600, 400
bg = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("demo")
event_texts = []

# create text in pygame: use Font
font = pygame.font.Font(None, 20) #the first argument: font name, the second argument: font size

line_height = font.get_linesize()

position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position = position + line_height

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()
