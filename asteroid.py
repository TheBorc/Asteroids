from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(50, 20)
            rotation_plus = self.velocity.rotate(+random_angle)
            rotation_minus = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_plus = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_minus = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_plus.velocity = rotation_plus * 1.2
            new_asteroid_minus.velocity = rotation_minus * 1.2
            return new_asteroid_plus, new_asteroid_minus

    def update(self, dt):
        self.position += self.velocity * dt
