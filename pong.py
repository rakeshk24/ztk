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

"""
design plan
2 players
2 scores
2 paddles - coordiantes stored as list for each
paddle - starting position coordinates, width, height
1 ball - coordinates stroes as list
paddles move vertically only - so x stays constant
ball movement - modify coordinates based on speed
UI elements - screen, black color, paddles and ball - white color
main logic:
    vertical rebound - compare the y coordinates of ball and screen
    players move the paddles using keyboard keys
    horizontal rebound - work with positions of the ball with that of paddles
    if ball reaches either side edges, a player scores a point
    restart the game when a player scores a point
    fix a max score for the game to be over
"""

import pygame

#constants
FPS = 40
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SPEED = 5 # constant that speed of ball movement

#colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)

#players
#player_1
#player_2

#player scores
player1_score = 0
player2_score = 0
pygame.font.init()
style = pygame.font.Font(None, 50)

#paddles
paddle_width = 25
paddle_height = 75

paddle1_pos = [20, SCREEN_HEIGHT/2]
paddle2_pos = [SCREEN_WIDTH-20-paddle_width, SCREEN_HEIGHT/2]
paddle1 = pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height)
paddle2 = pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height)

#ball
ball_radius = 20
ball_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
ball_speed = [SPEED, SPEED]

#UI elements
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Pong")
clock = pygame.time.Clock()

paddle1_ui = pygame.draw.rect(screen, WHITE, paddle1)
paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
ball = pygame.draw.circle(screen, WHITE, (ball_pos[0], ball_pos[1]), ball_radius)

#functions
def move_ball():
    global ball_pos, ball_speed, player1_score, player2_score
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] <= 10 or ball_pos[1] >= SCREEN_HEIGHT - 10:
        ball_speed[1] = -ball_speed[1]

    elif ball_pos[0] <= paddle1_pos[0] and paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1] + paddle_height:
        ball_speed[0] = -ball_speed[0]

    elif ball_pos[0] >= paddle2_pos[0] and paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1] + paddle_height:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[0] <= 0:
        player2_score += 1
    if ball_pos[0] >= SCREEN_WIDTH:
        player1_score += 1

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
    #setup UI
    screen.fill(BLACK)
    paddle1_ui = pygame.draw.rect(screen, WHITE, paddle1)
    paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
    ball = pygame.draw.circle(screen, WHITE, (ball_pos[0], ball_pos[1]), ball_radius)
    
    #move ball
    move_ball()

    #handle keyboard events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2_pos = (paddle2_pos[0], paddle2_pos[1] - SPEED)
        paddle2 = pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height)
        paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
    elif keys[pygame.K_DOWN]:
        paddle2_pos = (paddle2_pos[0], paddle2_pos[1] + SPEED)
        paddle2 = pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height)
        paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
    if keys[pygame.K_w]:
        paddle1_pos = (paddle1_pos[0], paddle1_pos[1] - SPEED)
        paddle1 = pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height)
        paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
    elif keys[pygame.K_s]:
        paddle1_pos = (paddle1_pos[0], paddle1_pos[1] + SPEED)
        paddle1 = pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height)
        paddle2_ui = pygame.draw.rect(screen, WHITE, paddle2)
    
    player1_text = style.render(str(player1_score), True, WHITE)
    player2_text = style.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (SCREEN_WIDTH/4, 20))
    screen.blit(player2_text, (SCREEN_WIDTH*3/4, 20))
    
    pygame.display.update()
    clock.tick(FPS)

