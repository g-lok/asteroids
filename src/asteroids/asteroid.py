import pygame
from asteroids.circleshape import CircleShape
from asteroids.logger import log_event
from asteroids.cnst import (
    ASTEROID_MIN_RADIUS,
    LINE_WIDTH,
)
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        incr_speed_scale = 1.2

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rnd_angle = int(random.uniform(20, 50))
        astr1_vector = self.velocity.rotate(rnd_angle)
        astr2_vector = self.velocity.rotate(-rnd_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        astr1 = Asteroid(self.position.x, self.position.y, radius)
        astr2 = Asteroid(self.position.x, self.position.y, radius)
        astr1.velocity = astr1_vector * incr_speed_scale
        astr2.velocity = astr2_vector * incr_speed_scale
