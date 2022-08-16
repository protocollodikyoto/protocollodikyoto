import pygame, sys, random

player_points = 0
opponent_points = 0

def ball_animation():
    global ball_speed_x, ball_speed_y, player_points, opponent_points 
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1    
    if ball.left <= 0:
        ball_restart()
        player_points += 1
    if ball.right >= screen_width:
        ball_restart()
        opponent_points += 1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -=opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.y = screen_height/2 - 15
    ball.x = screen_width/2 - 15
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def add_points():
    global user, opponent
    user = font.render(f"Player: {player_points}", 1, (255,255,255))
    opponent_p = font.render(f"Opponent: {opponent_points}", 1, (255,255,255))
    screen.blit(user,  (screen_width/2 + 10, 10))
    screen.blit(opponent_p,  (10 , 10))
    pygame.display.flip()


# General setup
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)
# Set up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10, 140)
opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7 

while True:
    # Handlig input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    ball_animation()
    add_points()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating th window
    clock.tick(60)