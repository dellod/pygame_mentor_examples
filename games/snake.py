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

    # Game over checker variable
    is_game_over = False

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

        # 2. Update Display
        X_POS += X_UPDATE
        Y_POS += Y_UPDATE
        display.fill(BLACK)
        pygame.draw.rect(display, GREEN, [X_POS, Y_POS, SNAKE_SIZE[0], SNAKE_SIZE[1]])
        pygame.display.update()
        clock.tick(CLOCK_TICK_SPEED)

    # Close and clean up
    pygame.quit()
    quit()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
