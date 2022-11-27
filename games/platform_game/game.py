# !/usr/bin/env python3
# @file game.py
# SCRP: Main Game Class
# Daryl Dang

# IMPORTS
import pygame

import constants


# CLASS DEFINITIONS
class Game:
    """
    A class used to run and compile the main game.

    ...

    Attributes
    ----------
    display : pygame.Surface
        pygame display of the game.
    clock : pygame.time.Clock
        clock of the game.
    running : bool
        boolean value that indicates whether the game is running or not.

    Methods
    -------
    check_events()
    run()
    close()
    """
    def __init__(self):
        # Initialize pygame and display window
        pygame.init()
        self.display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Platform Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Check events
            self.check_events()

            # Update pygame window
            pygame.display.update()

    def check_events(self):
        # Check events
        for event in pygame.event.get():
            # Quit when the user presses the X at the top right
            if event.type == pygame.QUIT:
                self.running = False

    def close(self):
        pygame.quit()
