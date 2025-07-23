#!/usr/bin/env python
from engine import app

if __name__ == '__main__':
    pacman = app.Application('pacman', 1280, 720)
    pacman.run()