
import pygame
import constants
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation: float = 0.0
        self.shooting_timer = 0.0


# Define triangle shape for the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) # Use 255, 255, 255 for white

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # HANDLE MOVEMENT INPUT
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(dt * -1)


        # HANDLE SHOOT INPUT
        if keys[pygame.K_SPACE]:
            if self.shooting_timer <= 0:
                # If the shooting timer is less than or equal to 0, the player can shoot
                # The timer is then set to the cooldown time
                self.shooting_timer = PLAYER_SHOOT_COOLDOWN
                # Call the shoot method
                self.shoot()
            elif self.shooting_timer > 0:
                print("Shoot is on cooldown")

        # HANDLE SHOOT COOLDOWN
        if self.shooting_timer > 0:
            # If the shooting timer is greater than 0, decrement it
            self.shooting_timer -= dt
            # Ensure the shooting timer does not go below 0
            if self.shooting_timer < 0:
                self.shooting_timer = 0 

        # Exit game if the player presses ESC
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

   
   
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        # Create a shot object and return it
        print("Shot fired!")
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            # Create a direction vector pointing in the direction the player is facing
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
         # Add the shot to your shots group - but you need a reference to it
        return new_shot