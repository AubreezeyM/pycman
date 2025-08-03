import pygame
import pygame.locals
from PIL.Image import isImageType
from pygame import K_RIGHT

from .entity import Entity
from .components import Component, SpriteComponent, VelocityComponent
from .systems import RenderSystem, MovementSystem, SystemManager

class Application:
    def __init__(self, title: str, width: int, height: int):
        pygame.init()
        self._RUNNING: bool = False
        self.title = title
        self.windowWidth = width
        self.windowHeight = height
        self._Window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.fpsClock = pygame.time.Clock()
        self.font = pygame.font.SysFont('adwaitamono.ttf', 18, bold=True)

        self.system_manager = SystemManager()
        self.system_manager.add_system(RenderSystem(self._Window))
        self.system_manager.add_system(MovementSystem())

        pygame.display.set_caption(self.title)

    def create_entity(self, sprite: pygame.Surface) -> Entity:
        entity = Entity()
        entity.add_component(SpriteComponent(sprite))
        entity.add_component(VelocityComponent())
        self.system_manager.add_entity(entity)
        return entity

    def run(self) -> None:
        self._RUNNING = True

        while self._RUNNING:
            self._Window.fill((0, 0, 0))
            fps = self.font.render(str(int(self.fpsClock.get_fps())), True, pygame.Color((255, 255, 255)))
            fps_rect = fps.get_rect()
                                     
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    self._RUNNING = False

            self._Window.blit(fps, fps_rect)
            self.system_manager.update()

            pygame.display.update()
            self.fpsClock.tick()
        return None
