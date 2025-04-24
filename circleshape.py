import pygame

# Base class for our game objects 

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        # Sub-classe must override this method.
        pass

    def udpate(self, dt):
        # Sub-class must override this method.
        pass

    # Getters and Setters
    def get_position(self):
        return self.position
    
    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y

    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, x, y):
        self.velocity.x = x
        self.velocity.y = y

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius


    