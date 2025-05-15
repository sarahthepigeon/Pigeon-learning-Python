import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

while True: #main loop of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #填充背景
    screen.fill((0, 0, 0))
    #获取鼠标位置并画出
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    pygame.draw.circle(screen, (255, 200, 200), mouse_pos, 5)
    # 更新屏幕
    pygame.display.flip()
    time.sleep(1/60)
