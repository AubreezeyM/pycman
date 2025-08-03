import abc

import pygame

from .components import Component, SpriteComponent
from .entity import Entity

class System(abc.ABC):
    _tracked_components: set[type[Component]] = set()

    @classmethod
    def track_component(cls, component_type: type[Component]) -> None:
        cls._tracked_components.add(component_type)

class RenderSystem(System):
    def __init__(self, screen: pygame.Surface):
        self.entities = set()
        self.screen: pygame.Surface = screen
        self.track_component(SpriteComponent)

    def update(self) -> None:
        for entity in self.entities:
            sprite = entity.get_component(SpriteComponent)
            self.screen.blit(sprite.sprite, (sprite.x, sprite.y))

    def add(self, entity: Entity) -> None:
        if all(entity.get_component(t) for t in self._tracked_components):
            self.entities.add(entity)


