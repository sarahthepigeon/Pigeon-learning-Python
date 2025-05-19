import sys
import pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
bg = (255, 255, 255)
speed = [0, 0]
old_speed = [0, 0]

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("control_the_turtle")

turtle = pygame.image.load("turtle.png")
position = turtle.get_rect()

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

pause = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            if event.key == K_SPACE:
                pause += 1
                # if stop / pause:
                if pause % 2 != 0:
                    old_speed = speed
                    speed = [0, 0]
                # if go / not pause:
                else:

                    speed = old_speed
            else:
                if event.key == K_LEFT:
                    speed = [-5, 0]
                    turtle = l_head
                if event.key == K_RIGHT:
                    speed = [5, 0]
                    turtle = r_head
                if event.key == K_UP:
                    speed = [0, -5]
                if event.key == K_DOWN:
                    speed = [0, 5]



    position = position.move(speed)

    if position.left < 0 or position.right > width:
        speed[0] = -speed[0]
    if position.bottom > height or position.top < 0:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, position)

    pygame.display.flip()

    clock.tick(30)
