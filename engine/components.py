from dataclasses import dataclass

import abc
import pygame

class Component(abc.ABC):
    pass

class SpriteComponent(Component):
    def __init__(self, sprite):
        self.sprite: pygame.Surface = sprite
        self.x: int = 300
        self.y: int = 300


