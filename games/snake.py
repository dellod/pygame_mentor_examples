# !/usr/bin/env python3
# @file snake.py
# SCRP: Snake Game
# Daryl Dang

####################################################################################################
# Snake
# TODO: insert snake description
####################################################################################################

# IMPORTS
import pygame
import random
import sys

### GLOBALS
# Clock
CLOCK_TICK_SPEED = 10

# Screen size
SCREEN_WIDTH    = 800
SCREEN_HEIGHT   = 800

# Colours
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)

# Positions and sizes
SNAKE_SIZE      = (40, 40)
MOVEMENT_SIZE   = 40
NO_MOVEMENT     = 0
X_POS           = SCREEN_WIDTH / 2
Y_POS           = SCREEN_HEIGHT / 2
X_UPDATE        = 0
Y_UPDATE        = 0

### FUNCTIONS
def create_message(message: str,
                   colour: tuple,
                   x_pos: float,
                   y_pos: float,
                   display: pygame.Surface,
                   font_style: pygame.font.Font) -> None:
    """Writes message to display window given the colour and position."""
    msg = font_style.render(message, True, colour)
    display.blit(msg, [x_pos, y_pos])


def generate_random_food_position() -> tuple:
    food_pos = \
        (round(random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE[0]) / SNAKE_SIZE[0]) * SNAKE_SIZE[0],
         round(random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE[1]) / SNAKE_SIZE[1]) * SNAKE_SIZE[1])
    return food_pos


def check_grid_collision(snake_pos: tuple, food_pos: tuple):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False


def main() -> None:
    """Main entry point for program"""
    # Declare globals that will be used in function
    global X_POS, Y_POS, X_UPDATE, Y_UPDATE

    # Declare clock
    clock = pygame.time.Clock()

    # Initialize pygame window
    pygame.init()
    display = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size
    pygame.display.update()
    pygame.display.set_caption("Snake Game")

    # Set up font style
    font_style = pygame.font.SysFont(None, 50)

    # Food variables
    food_pos = generate_random_food_position()

    # Important info variables
    score = 0

    # Important flag variables for checking states
    is_game_over = False
    did_player_lose = False

    # Game loop - loop until the user quits the game
    while not is_game_over:
        # 1. Detect Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit when the user presses the X at the top right
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                # User has pressed the key, now check which key has been pressed
                if event.key == pygame.K_LEFT:
                    # Move snake to the left
                    X_UPDATE = -MOVEMENT_SIZE
                    Y_UPDATE = NO_MOVEMENT
                if event.key == pygame.K_RIGHT:
                    # Move snake to the right
                    X_UPDATE = MOVEMENT_SIZE
                    Y_UPDATE = NO_MOVEMENT
                if event.key == pygame.K_UP:
                    # Move snake to the up
                    X_UPDATE = NO_MOVEMENT
                    Y_UPDATE = -MOVEMENT_SIZE
                if event.key == pygame.K_DOWN:
                    # Move snake to the down
                    X_UPDATE = NO_MOVEMENT
                    Y_UPDATE = MOVEMENT_SIZE

        # 2. Check conditions
        if X_POS > SCREEN_WIDTH or X_POS < 0 or Y_POS > SCREEN_HEIGHT or Y_POS < 0:
            did_player_lose = True

        # 3. Update Display
        # Draw background
        display.fill(BLACK)

        # Draw scoreboard
        score_message = "Score: " + str(score)
        create_message(score_message, WHITE, 10, 10, display, font_style)

        # Draw snake
        pygame.draw.rect(display, GREEN, [X_POS, Y_POS, SNAKE_SIZE[0], SNAKE_SIZE[1]])

        # Draw food
        pygame.draw.rect(display, RED, [food_pos[0], food_pos[1], SNAKE_SIZE[0], SNAKE_SIZE[1]])

        # Check if snake is on top of food
        if check_grid_collision((X_POS, Y_POS), food_pos):
            score += 1
            food_pos = generate_random_food_position()

        # Increase length of snake
        # TODO

        # Check if player lost
        if did_player_lose:
            create_message("You lost!", RED, SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2, display, font_style)
            # TODO: They have to press a key here to restart the game
        else:
            X_POS += X_UPDATE
            Y_POS += Y_UPDATE
        pygame.display.update()
        clock.tick(CLOCK_TICK_SPEED)

    # Close and clean up
    pygame.quit()
    quit()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
