import pygame
import random

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (135, 206, 235)
COLOR_NULL = (0, 0, 0, 0)

size = (650, 780)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2021.01.30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
score_text = score_font.render('00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (110, 50)

# life text
player_life_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
player_life_text = score_font.render('00', True, COLOR_WHITE, COLOR_BLACK)
player_life_text_rect = score_text.get_rect()
player_life_text_rect.center = (540, 50)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')


# time between collisions
last_bounce_time = 0
bounce_interval = 50
bounce_check = 0

game_over = False

# player paddle position
player_1_x = 325
player_1_y = 670
player_1_width = 80
player_1_height = 15

# player paddle movement
player_1_move_right = False
player_1_move_left = False


def initialize_ball_speed():
    ball_x = 318
    ball_y = 400
    ball_dx = random.randint(1, 3)
    ball_dy = 6 - ball_dx
    return ball_dx, ball_dy


# ball position and speed
ball_x = 318
ball_y = 400
ball_dx, ball_dy = initialize_ball_speed()
ball_dx = ball_dx * random.choice([1, -1])


def create_rect(color, x, y, ):
    block = pygame.draw.rect(screen, color, (x, 100 + y, 40, 15))
    return block


# bricks create
transparent_block = pygame.draw.rect(screen, COLOR_NULL, (0, 0, 0, 0))

red = []
for n in range(2):
    for c in range(14):
        red_block = create_rect(COLOR_RED, 12 + c * 45, n * 20)
        red.append(red_block)


orange = []
for n in range(2):
    for c in range(14):
        orange_block = create_rect(COLOR_ORANGE, 12 + c * 45, 40 + n * 20)
        orange.append(orange_block)


green = []
for n in range(2):
    for c in range(14):
        green_block = create_rect(COLOR_GREEN, 12 + c * 45, 80 + n * 20)
        green.append(green_block)


yellow = []
for n in range(2):
    for c in range(14):
        yellow_block = create_rect(COLOR_YELLOW, 12 + c * 45, 120 + n * 20)
        yellow.append(yellow_block)


def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_y = 400
    ball_x = 240
    ball_dx, ball_dy = initialize_ball_speed()
    ball_dx = ball_dx * random.choice([1, -1])
    scoring_sound_effect.play()


# player life
player_life = 3

# score
score = 0
score_max = 448

# game loop
game_loop = True
game_clock = pygame.time.Clock()
game_over = False

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
            if event.key == pygame.K_SPACE:
                player_1_reset = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False
            if event.key == pygame.K_LEFT:
                player_1_move_left = False
            if event.key == pygame.K_SPACE:
                player_1_reset = False

    if game_over == False:
        # clear screen
        screen.fill(COLOR_BLACK)

        # player paddle
        player_paddle = pygame.draw.rect(screen, COLOR_BLUE,[player_1_x, player_1_y, player_1_width, player_1_height], 0)

        # ball create
        ball = pygame.draw.rect(screen, COLOR_BLUE, [ball_x, ball_y, 13, 13], 0)

        # update score
        score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)

        #update life
        player_life_text = score_font.render(str(player_life), True, COLOR_WHITE, COLOR_BLACK)

        # collision brick
        if bounce_check == 1:
            if ball.collidelist(red) != -1:
                current_time = pygame.time.get_ticks()
                if current_time - last_bounce_time >= bounce_interval:
                    if ball_dy == - abs(ball_dy):
                        if ball_dy > - 10:
                            ball_dy = - 10
                            ball_dy *= -1
                            red[ball.collidelist(red)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 7
                        else:
                            ball_dy *= -1
                            red[ball.collidelist(red)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 7
                    else:
                        if ball_dy < 10:
                            ball_dy = 10
                            ball_dy *= -1
                            red[ball.collidelist(red)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 7
                        else:
                            ball_dy *= -1
                            red[ball.collidelist(red)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 7

            if ball.collidelist(orange) != -1:
                current_time = pygame.time.get_ticks()
                if current_time - last_bounce_time >= bounce_interval:
                    if ball_dy == - abs(ball_dy):
                        if ball_dy > - 9:
                            ball_dy = - 9
                            ball_dy *= -1
                            orange[ball.collidelist(orange)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 5
                        else:
                            ball_dy *= -1
                            orange[ball.collidelist(orange)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 5
                    else:
                        if ball_dy < 9:
                            ball_dy = 9
                            ball_dy *= -1
                            orange[ball.collidelist(orange)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 5
                        else:
                            ball_dy *= -1
                            orange[ball.collidelist(orange)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 5

            if ball.collidelist(green) != -1:
                current_time = pygame.time.get_ticks()
                if current_time - last_bounce_time >= bounce_interval:
                    if ball_dy == - abs(ball_dy):
                        if ball_dy > - 8:
                            ball_dy = - 8
                            ball_dy *= -1
                            green[ball.collidelist(green)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 3
                        else:
                            ball_dy *= -1
                            green[ball.collidelist(green)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 3
                    else:
                        if ball_dy < 8:
                            ball_dy = 8
                            ball_dy *= -1
                            green[ball.collidelist(green)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 3
                        else:
                            ball_dy *= -1
                            green[ball.collidelist(green)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 3

            if ball.collidelist(yellow) != -1:
                current_time = pygame.time.get_ticks()
                if current_time - last_bounce_time >= bounce_interval:
                    if ball_dy == - abs(ball_dy):
                        if ball_dy > -6:
                            ball_dy = -6
                            ball_dy *= -1
                            yellow[ball.collidelist(yellow)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 1
                        else:
                            ball_dy *= -1
                            yellow[ball.collidelist(yellow)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 0
                            bounce_sound_effect.play()
                            score += 1
                    else:
                        if ball_dy < 6:
                            ball_dy = 6
                            ball_dy *= -1
                            yellow[ball.collidelist(yellow)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 1
                        else:
                            ball_dy *= -1
                            yellow[ball.collidelist(yellow)] = transparent_block
                            last_bounce_time = current_time
                            bounce_check = 1
                            bounce_sound_effect.play()
                            score += 1

        # drawing bricks
        for red_block in red:
            pygame.draw.rect(screen, COLOR_RED, red_block)

        for orange_block in orange:
            pygame.draw.rect(screen, COLOR_ORANGE, orange_block)

        for green_block in green:
            pygame.draw.rect(screen, COLOR_GREEN, green_block)

        for yellow_block in yellow:
            pygame.draw.rect(screen, COLOR_YELLOW, yellow_block)

        # ball collision with the wall
        if ball_x > 637:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()
        elif ball_x <= 0:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()
        elif ball_y <= 0:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dy *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball.colliderect(player_paddle):
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx = (ball_x + 7 - (player_1_x + player_1_width / 2)) / (player_1_width / 9)
                ball_dy = -abs(ball_dy)
                bounce_sound_effect.play()
                last_bounce_time = current_time
                bounce_check = 1

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # ball reset
        if ball_y >= 780 - 13:
            reset_ball()
            player_life -= 1

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
        if player_1_x >= 570:
            player_1_x = 570

        # player 1 collision with left wall
        if player_1_x <= 0:
            player_1_x = 0

        if player_life == 0 or score == score_max:
            game_over = True

        screen.blit(score_text, score_text_rect)
        screen.blit(player_life_text, player_life_text_rect)

    if game_over:
        if player_1_move_right or player_1_move_left:
            red = []
            for n in range(2):
                for c in range(14):
                    red_block = create_rect(COLOR_RED, 12 + c * 45, n * 20)
                    red.append(red_block)

            orange = []
            for n in range(2):
                for c in range(14):
                    orange_block = create_rect(COLOR_ORANGE, 12 + c * 45, 40 + n * 20)
                    orange.append(orange_block)

            green = []
            for n in range(2):
                for c in range(14):
                    green_block = create_rect(COLOR_GREEN, 12 + c * 45, 80 + n * 20)
                    green.append(green_block)

            yellow = []
            for n in range(2):
                for c in range(14):
                    yellow_block = create_rect(COLOR_YELLOW, 12 + c * 45, 120 + n * 20)
                    yellow.append(yellow_block)
            bounce_check = 1
            score = 0
            player_life = 3
            game_over = False
            #realocating the player
            player_1_x = 325
            player_1_y = 670


        # clear screen
        screen.fill(COLOR_BLACK)

        # player paddle
        player_paddle = pygame.draw.rect(screen, COLOR_BLUE,
                                         [0, player_1_y, 650, player_1_height], 0)

        # ball create
        ball = pygame.draw.rect(screen, COLOR_BLUE, [ball_x, ball_y, 13, 13], 0)

        # update score
        score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)

        # update life
        player_life_text = score_font.render(str(player_life), True, COLOR_WHITE, COLOR_BLACK)

        # collision brick
        if ball.collidelist(red) != -1:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                last_bounce_time = current_time
                ball_dy *= -1

        if ball.collidelist(orange) != -1:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                last_bounce_time = current_time
                ball_dy *= -1

        if ball.collidelist(green) != -1:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                last_bounce_time = current_time
                ball_dy *= -1

        if ball.collidelist(yellow) != -1:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                last_bounce_time = current_time
                ball_dy *= -1

        # drawing bricks
        for red_block in red:
            pygame.draw.rect(screen, COLOR_RED, red_block)

        for orange_block in orange:
            pygame.draw.rect(screen, COLOR_ORANGE, orange_block)

        for green_block in green:
            pygame.draw.rect(screen, COLOR_GREEN, green_block)

        for yellow_block in yellow:
            pygame.draw.rect(screen, COLOR_YELLOW, yellow_block)

        # ball collision with the wall
        if ball_x > 637:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()
        elif ball_x <= 0:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()
        elif ball_y <= 0:
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dy *= -1
                last_bounce_time = current_time
                bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball.colliderect(player_paddle):
            current_time = pygame.time.get_ticks()
            if current_time - last_bounce_time >= bounce_interval:
                ball_dx *= -1
                ball_dy *= -1
                bounce_sound_effect.play()
                last_bounce_time = current_time

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # ball reset
        if ball_y >= 780 - 13:
            reset_ball()
            player_life -= 1

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
        if player_1_x >= 570:
            player_1_x = 570

        # player 1 collision with left wall
        if player_1_x <= 0:
            player_1_x = 0

        screen.blit(score_text, score_text_rect)
        screen.blit(player_life_text, player_life_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()