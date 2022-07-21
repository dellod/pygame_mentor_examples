# !/usr/bin/env python3
# @file template.py
# SCRP: General Template For PyGame Files
# Daryl Dang

####################################################################################################
# This file will serve as a template for starting out projects and setting up the PyGame window.
# Note: examples will LOOSELY follow PEP 8 guidelines.
# See https://peps.python.org/pep-0008/ for more detailed guidelines.
####################################################################################################

# IMPORTS
import pygame
import sys

# GLOBALS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# FUNCTIONS


def main() -> None:
    """ Main entry point for program"""
    # Initialize pygame window
    pygame.init()
    display = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size
    pygame.display.update()
    pygame.display.set_caption("INSERT NAME OF GAME HERE")
    is_game_over = False

    # Game loop - loop until the user quits the game
    while not is_game_over:
        for event in pygame.event.get():
            # Quit when the user presses the X at the top right
            if event.type == pygame.QUIT:
                is_game_over = True

    # Close and clean up
    pygame.quit()
    quit()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
