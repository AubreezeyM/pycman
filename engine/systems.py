import abc

import pygame

from .components import Component, SpriteComponent
from .entity import Entity

class System(abc.ABC):
    pass

class RenderSystem(System):
    def __init__(self, screen: pygame.Surface):
        self.entities = set()
        self.screen: pygame.Surface = screen

    def update(self) -> None:
        for entity in self.entities:
            sprite = entity.get_component(SpriteComponent)
            self.screen.blit(sprite.sprite, (sprite.x, sprite.y))

    def add(self, entity: Entity) -> None:
        if all(entity.get_component(t) for t in self.entities):
            self.entities.add(entity)


