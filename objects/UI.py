import pygame


class UIElement:
    text = None
    percent = None
    x = 0
    y = 0

    def draw(self, screen):
        ...


class HPBar(UIElement):
    percent = 1

    def __init__(self, text, position):
        self.text = text
        self.x = position['x']
        self.y = position['y']
    
    def draw(self, screen):
        end_pos = (
            self.x + self.percent*200,
            self.y,
        )
        pygame.draw.line(screen, "red", (self.x, self.y), end_pos, 10)
