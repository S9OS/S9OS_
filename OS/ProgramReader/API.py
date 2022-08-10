import pygame

class Window(pygame.Surface):
    ROUNDED = "ROUNDED"
    BOXED = "BOXED"

    def __init__(self, width, height, type, name, icon):
        super().__init__((width, height))
        self.width = width
        self.height = height #lol
        self.type = type
        self.name = name
        self.icon = icon
        self.icon_image = pygame.image.load(icon).convert_alpha()
        self.cooldown = 0
        self.stored = {}

    def update_win(self, new_width, new_height, new_name, new_icon):
        if self.cooldown >= 10:
            self.width = new_width
            self.height = new_height
            self.name = new_name
            self.icon = new_icon
            self.icon_image = pygame.image.load(new_icon).convert_alpha()
        else:
            pass

    def store(self, function):
        def payload(_type):
            print(f"Preparing to store function type {_type}")
            self.stored[_type] = function
            print(f"Stored function type {_type}")
        return payload

    def draw(self):
        # TODO: implement the drawing method. (Implement Buttons first or layout IDK
        pass
