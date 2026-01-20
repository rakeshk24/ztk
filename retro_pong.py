#requirememnts
# screen
# background
# 2 scores at the top
# 2 paddles - one on either side of the screen
# paddles can move vertically only
# 1 ball
# ball when in contact with paddle, rebounds
# if not, the paddle loses the game
# the other paddle gets a point
# game starts when enter is hit
# game stops when esc is hit

import pygame
import random

screen = pygame.display.set_mode((700, 500))
title = pygame.display.set_caption("retro pong game")
background = pygame.image.load("nature.jpg")
background = pygame.transform.scale(background, (700, 500))
clock = pygame.time.Clock()

color = pygame.Color(255, 255, 255)
y1 = 250
y2 = 250
cx = 300
cy = 300
random_num = random.randint(10, 50)

var = True
while var:
    #screen.blit(background, (0,0))
    screen.fill((0,0,0))

    rect_1 = pygame.Rect(100, y1, 25, 75)
    rect_2 = pygame.Rect(550, y2, 25, 75)
    pygame.draw.rect(screen, color, rect_1)
    pygame.draw.rect(screen, color, rect_2)
    ball_pos = [700/2, 500/2]
    ball_speed = [5, 5]
    pygame.draw.circle(screen, color, (ball_pos[0], ball_pos[1]), 20)

    def change_pos_by_add(ball_pos, ball_speed):
        return list(ball_pos[0] + ball_speed[0], ball_pos[1] + ball_speed[1])

    def change_pos_by_sub(ball_pos, ball_speed):
        return list(ball_pos[0] - ball_speed[0], ball_pos[1] - ball_speed[1])
    
    rand_funcs_list = [change_pos_by_add, change_pos_by_sub]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        random.choice(rand_funcs_list)
    if keys[pygame.K_UP]:
        y2 -= 10
    if keys[pygame.K_DOWN]:
        y2 += 10
    if keys[pygame.K_w]:
        y1 -= 10
    if keys[pygame.K_s]:
        y1 += 10        
    pygame.display.update()
    clock.tick(30)