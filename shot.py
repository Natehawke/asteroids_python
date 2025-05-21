import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    """
    Class representing a shot in the game.
    Inherits from CircleShape to represent the shot's shape and position.
    """

    def __init__(self, x, y, radius):
        """
        Initialize the shot with its position and radius.

        :param x: The x-coordinate of the shot's center.
        :param y: The y-coordinate of the shot's center.
        :param radius: The radius of the shot.
        """
        super().__init__(x, y, radius)
        self.radius = constants.SHOT_RADIUS
        self.color = (255, 0, 0)  # Red color for the shot
        self.width = 2 # Width of the shot's outline
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen): 
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt