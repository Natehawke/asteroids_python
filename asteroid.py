
import pygame
import constants
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    """
    Class representing an asteroid in the game.
    Inherits from CircleShape to represent the asteroid's shape and position.
    """

    def __init__(self, x, y, radius):
        """
        Initialize the asteroid with its position and radius.

        :param x: The x-coordinate of the asteroid's center.
        :param y: The y-coordinate of the asteroid's center.
        :param radius: The radius of the asteroid.
        """
        super().__init__(x, y, radius)
        self.radius = radius
        self.color = (255, 255, 255)  # White color for the asteroid
        self.width = 2 # Width of the asteroid's outline
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen): 
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt
       
    def split(self):

        new_asteroids = []

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []
        else:
            old_radius = self.radius
            
            random_angle = random.uniform(20, 50)
            # Create new asteroids with a random angle
            new_rotation_1 = self.velocity.rotate(random_angle)
            new_rotation_2 = self.velocity.rotate(-random_angle)

            # Create two new asteroids with a smaller radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = new_rotation_1 * 1.2
            new_asteroid_2.velocity = new_rotation_2 * 1.2

            # Add the new asteroids to the list
            new_asteroids.append(new_asteroid_1)
            new_asteroids.append(new_asteroid_2)

            self.kill()

            # Return the list of new asteroids
            return new_asteroids