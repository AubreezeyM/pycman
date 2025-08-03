import abc
from ssl import PEM_cert_to_DER_cert

import pygame

from .components import Component, SpriteComponent, VelocityComponent, InputComponent
from .entity import Entity

class System(abc.ABC):
    # Set required components for each system
    _tracked_components: set[type[Component]] = set()

    @classmethod
    def track_component(cls, component_type: type(Component)) -> None:
        cls._tracked_components.add(component_type)

class SystemManager:
    def __init__(self):
        self._systems: list[System] = []
        self._entity_cache: dict[type[System], set[Entity]] = {}

    def add_system(self, system: System) -> None:
        self._systems.append(system)
        self._entity_cache[type(system)] = set()

    def add_entity(self, entity: Entity) -> None:
        for system in self._systems:
            if self._entity_qualifies(system, entity):
                self._entity_cache[type(system)].add(entity)
                system.add(entity)  # Optional: Notify system directly

    def remove_entity(self, entity: Entity) -> None:
        for system_type, entities in self._entity_cache.items():
            if entity in entities:
                entities.remove(entity)

    def update(self) -> None:
        for system in self._systems:
            system.update()

    def _entity_qualifies(self, system: System, entity: Entity) -> bool:
        return all(
            entity.get_component(comp_type)
            for comp_type in getattr(system, "_tracked_components", set())
        )


class RenderSystem(System):
    def __init__(self, screen: pygame.Surface):
        self.entities = set()
        self.screen: pygame.Surface = screen
        self.track_component(SpriteComponent)

    def update(self) -> None:
        for entity in self.entities:
            sprite = entity.get_component(SpriteComponent)
            self.screen.blit(sprite.sprite, (entity.x_pos, entity.y_pos))

    def add(self, entity: Entity) -> None:
        if entity.get_component(SpriteComponent):
            self.entities.add(entity)

class MovementSystem(System):
    def __init__(self):
        self.entities = set()
        self.track_component(VelocityComponent)

    def update(self) -> None:
        for entity in self.entities:
            velocity = entity.get_component(VelocityComponent)
            if velocity:
                entity.x_pos += velocity.vx
                entity.y_pos += velocity.vy

    def add(self, entity: Entity) -> None:
        if entity.get_component(VelocityComponent):
            self.entities.add(entity)

class InputSystem(System):
    def __init__(self):
        self.track_component(VelocityComponent)
        self.track_component(InputComponent)
        self.entities = set()

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        for entity in self.entities:
            velocity = entity.get_component(VelocityComponent)

            if keys[pygame.K_LEFT]:
                velocity.vx = -1
            elif keys[pygame.K_RIGHT]:
                velocity.vx = 1
            elif keys[pygame.K_UP]:
                velocity.vy = -1
            elif keys[pygame.K_DOWN]:
                velocity.vy = 1

    def add(self, entity: Entity) -> None:
        if entity.get_component(InputComponent):
            self.entities.add(entity)

