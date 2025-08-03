from dataclasses import dataclass

import abc
import pygame

@dataclass
class Component:
    def __init__(self):
        self._id: int = id(self)

    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id

class SpriteComponent(Component):
    def __init__(self, sprite: pygame.Surface):
        super().__init__()
        self.sprite = sprite

class VelocityComponent(Component):
    def __init__(self):
        super().__init__()
        self.vx: int = 0
        self.vy: int = 0


