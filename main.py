#!/usr/bin/env python
from engine.app import Application
import pygame

if __name__ == '__main__':
    game = Application('pacman', 1280, 720)
    pacman_sprite = pygame.image.load('assets/pacman-right/1.png')
    pacman = game.create_entity(pacman_sprite)

    game.run()