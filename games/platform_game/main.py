# !/usr/bin/env python3
# @file main.py
# SCRP: Platform Game - Run file
# Daryl Dang

# IMPORTS
import sys
from game import Game


def main() -> None:
    game = Game()
    game.run()
    game.close()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
