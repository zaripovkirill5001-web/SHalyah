import pygame
import math


class Player:
    image="☠️"
    position = {'x':None, 'y':None}
    rotation = math.pi/2

    velocity = 10
    rotation_velocity = math.pi

    def __init__(self):
        self.position['x'] = 400
        self.position['y'] = 400

    def handle_keys(self, dt): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotation -= self.rotation_velocity * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += self.rotation_velocity * dt
        if keys[pygame.K_UP]:
            self.position['x'] += self.velocity * math.cos(self.rotation)
            self.position['y'] += self.velocity * math.sin(self.rotation)
        if keys[pygame.K_DOWN]:
            self.position['x'] -= self.velocity * math.cos(self.rotation) * 0.2
            self.position['y'] -= self.velocity * math.sin(self.rotation) * 0.2

    def draw(self, screen):

        # pygame.draw.circle(screen, "red", (self.position['x'], self.position['y']), radius=10)
        # pygame.draw.rect(screen, "green", (10,10))
        end_pos = (
            self.position['x'] + 20*math.cos(self.rotation),
            self.position['y'] + 20*math.sin(self.rotation),
        )
        pygame.draw.line(screen, "green", (self.position['x'], self.position['y']), end_pos, 4)

        square_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
        square_surface.fill('green')
        rotated_surface = pygame.transform.rotate(square_surface, - self.rotation * 180 / math.pi)
        rotated_rect = rotated_surface.get_rect()
        rotated_rect.center = (self.position['x'], self.position['y'])
        screen.blit(rotated_surface, rotated_rect)
