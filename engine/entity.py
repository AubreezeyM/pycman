from .components import Component

from operator import itemgetter

class Entity:
    def __init__(self):
        self.components: list[Component] = []

    def add_component(self, component: Component):
        self.components.append(component)

    def remove_component(self, component: Component):
        if component in self.components:
            self.components.remove(component)