import pygame
import pygame.locals
from pygame.locals import *

from PIL import Image

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

        pygame.display.set_caption(self.title)

    def run(self) -> None:
        self._RUNNING = True
        pacman_sprite = Image.open('assets/pacman-right/1.png', 'r')
        pacman = GameObject(pacman_sprite)

        while self._RUNNING:
            self._Window.fill((0, 0, 0))
            fps = self.font.render(str(int(self.fpsClock.get_fps())), True, pygame.Color((255, 255, 255)))
            fps_rext = fps.get_rect()
            self._Window.blit(fps, fps_rext)                    
                                     
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return 0

            pygame.display.update()
            self.fpsClock.tick()

class GameObject:
    def __init__(self, x:int = 0, y:int = 0):
        self.x_pos = x
        self.y_pos = y
        self.components: list = []
        self.children: list = []
        self.parent = None

    def add_component(self, component):
        component.game_object = self
        self.components.append(component)

class RenderComponent:
    def __init__(self, sprite: Image):
        self.sprite = sprite
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.sprite, (self.game_object.x_pos, self.game_object.y_pos))