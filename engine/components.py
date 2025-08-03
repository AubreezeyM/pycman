from dataclasses import dataclass

import abc
import pygame

@dataclass
class Component:
    pass

class SpriteComponent(Component):
    def __init__(self, sprite):
        self.sprite: pygame.Surface = sprite
        self.x: int = 400
        self.y: int = 400
        self._id = id(self)

    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id


