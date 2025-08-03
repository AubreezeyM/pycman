from .components import Component

class Entity:
    def __init__(self):
        self.components = set()
        self.x_pos: int = 0
        self.y_pos: int = 0

    def add_component(self, component: Component) -> None:
        component.parent = self
        self.components.add(component)

    def remove_component(self, component: Component) -> None:
        if component in self.components:
            self.components.remove(component)

    def get_component(self, component_type: type) -> Component:
        for item in self.components:
            if isinstance(item, component_type):
                return item