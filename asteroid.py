import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new1_vector = self.velocity.rotate(angle)
            new2_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new1_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new2_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            self.kill()
            new1_asteroid.velocity = new1_vector * 1.2
            new2_asteroid.velocity = new2_vector * 1.2
            