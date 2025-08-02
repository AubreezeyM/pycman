import pygame
import pygame.locals

from .entity import Entity
from .components import SpriteComponent
from .systems import RenderSystem

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

        self.renderer = RenderSystem(self._Window)

        pygame.display.set_caption(self.title)

    def run(self) -> None:
        self._RUNNING = True
        pacman_sprite = pygame.image.load('assets/pacman-right/1.png')

        pacman = Entity()
        pacman.add_component(SpriteComponent(pacman_sprite))
        self.renderer.targets.add(pacman.components[0])

        while self._RUNNING:
            self._Window.fill((0, 0, 0))
            fps = self.font.render(str(int(self.fpsClock.get_fps())), True, pygame.Color((255, 255, 255)))
            fps_rect = fps.get_rect()
                                     
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    self._RUNNING = False

            self._Window.blit(fps, fps_rect)
            self.renderer.update()

            pygame.display.update()
            self.fpsClock.tick()
        return None
