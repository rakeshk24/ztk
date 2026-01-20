import pygame
import time

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Our game 1")
clock = pygame.time.Clock()
x = 100
y = 100
background = pygame.image.load("nature.jpg")
background = pygame.transform.scale(background, (700,500))
plane = pygame.image.load("plane2.jpeg")
plane = pygame.transform.scale(plane, (100,100))
#plane = pygame.transform.scale(pygame.image.load("plane.png"), (200,100))

var = True
while var:
    screen.blit(background,(0,0))
    screen.blit(plane, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 10:
        y -= 10
    if keys[pygame.K_DOWN] and y < 480-100:
        y += 10
    if keys[pygame.K_LEFT] and x > 10:
        x -= 10
    if keys[pygame.K_RIGHT] and x < 680-100:
        x += 10
    pygame.display.update()
    clock.tick(30)