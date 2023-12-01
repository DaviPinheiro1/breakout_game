import pygame
import random

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

size = (500, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2021.01.30")

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# time between collisions
last_bounce_time = 0
bounce_interval = 500

# player paddle position
player_1_x = 200
player_1_y = 670
player_1_width = 80
player_1_height = 15

# player paddle movement
player_1_move_right = False
player_1_move_left = False


def initialize_ball_speed():
    ball_dx = random.random()
    ball_dy= 2 - ball_dx

    return ball_dx, ball_dy


# ball position and speed
ball_x = 240
ball_y = 400
ball_dx, ball_dy = initialize_ball_speed()
ball_dx = ball_dx * random.choice([1, -1])
speed_max = 25


def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_y = 400
    ball_x = 240
    ball_dx, ball_dy = initialize_ball_speed()
    ball_dx = ball_dx * random.choice([1, -1])
    scoring_sound_effect.play()


# score
score = 0
score_max = 100

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_1_move_right = True
            if event.key == pygame.K_LEFT:
                player_1_move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False
            if event.key == pygame.K_LEFT:
                player_1_move_left = False

    if score < score_max:
        # clear screen
        screen.fill(COLOR_BLACK)

        # player paddle
        player_paddle = pygame.draw.rect(screen, COLOR_WHITE,
                                         [player_1_x, player_1_y, player_1_width, player_1_height], 0)

        # ball create
        ball = pygame.draw.rect(screen, COLOR_WHITE, [ball_x, ball_y, 13, 13], 0)

        # ball collision with the wall
        if ball_x > 487:
            ball_dx *= -1
            bounce_sound_effect.play()
        elif ball_x <= 0:
            ball_dx *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball.colliderect(player_paddle):
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx = (ball_x + 6.5 - (player_1_x + player_1_width / 2)) / (player_1_width / 9)
                ball_dy = -abs(ball_dy)
                bounce_sound_effect.play()
                last_bounce_time = current_time

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # ball reset
        if ball_y >= 762:
            reset_ball()

        # player 1 right movement
        if player_1_move_right:
            player_1_x += 5
        else:
            player_1_x += 0

        # player 1 left movement
        if player_1_move_left:
            player_1_x -= 5
        else:
            player_1_x += 0

        # player 1 collision with right wall
        if player_1_x >= 420:
            player_1_x = 420

        # player 1 collision with left wall
        if player_1_x <= 0:
            player_1_x = 0

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
