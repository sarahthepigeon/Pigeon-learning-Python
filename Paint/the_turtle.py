import pygame
import sys
# initialize Pygame
pygame.init()

# create the window
size = width, height = 800, 600
bg = (255, 255, 255)   # bg is a tuple
speed = [-2, 1]

screen = pygame.display.set_mode(size)  # 创建一个Surface对象 --> 一个白色的背景画布

pygame.display.set_caption("hello!!!")

turtle = pygame.image.load("turtle.png")

# get position of the turtle image
position = turtle.get_rect()

# the game begin
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # draw the background
    screen.fill(bg)
    # draw the turtle on the background
    screen.blit(turtle, position)

    # the double buffer thing
    pygame.display.flip()
    # related to the speed of the turtle
    pygame.time.delay(10)





