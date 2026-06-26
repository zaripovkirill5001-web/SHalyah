import pygame
import math


class Bullet:
    velocity = 250
    is_active = True
    def __init__(self, positions, rotate):
        self.position = positions
        self.rotation = rotate
    
    def handle_logic(self, dt):
        self.position['x'] += self.velocity * math.cos(self.rotation) * dt
        self.position['y'] += self.velocity * math.sin(self.rotation) * dt

        if self.position['x'] > 700 or self.position['x'] < 100:
            self.is_active = False
        if self.position['y'] > 700 or self.position['y'] < 100:
            self.is_active = False

    def draw(self, screen):
        if self.is_active:
            pygame.draw.circle(screen, "yellow", (self.position['x'], self.position['y']), 5)
            return self
        else:
            return None
