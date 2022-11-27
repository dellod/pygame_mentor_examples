# !/usr/bin/env python3
# @file main.py
# SCRP: Platform Game - Run file
# Daryl Dang

# IMPORTS
import pygame
import sys

def main() -> None:
    """Main entry point for program"""
    # Initialize pygame window
    pygame.init()

    # Close and clean up
    pygame.quit()
    quit()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
