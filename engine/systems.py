import abc

import pygame

from .components import SpriteComponent
from .entity import Entity


class System(abc.ABC):
    def update(self):
        pass

class RenderSystem(System):
    def __init__(self, screen: pygame.Surface):
        self.targets: set[SpriteComponent] = set()
        self.screen: pygame.Surface = screen

    def update(self):
        for target in self.targets:
            target_rect = target.sprite.get_rect()
            self.screen.blit(target.sprite, target_rect)

