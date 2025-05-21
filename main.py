# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# This is the main file for the asteroids game. It will run the game and handle all the events. 
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    
    # Create sprite groups for updatable and drawable objects
    # This is a good practice to keep track of all the objects that need to be updated and drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player_object = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    #asteroid_object = Asteroid(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = 20)

    AsteroidField.containers = updatable # We only add the asteroid to the updatable group
    asteroid_field_object = AsteroidField()

    # Set up the shot object and group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    shot_object = Shot

    # Initialize the timer
    timer = pygame.time.Clock()

    running = True
    while running:
        # Calculate dt inside the game loop
        dt = timer.get_time() / 1000.0

        # Make the close button on the window work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            
        screen.fill((0, 0, 0))  # Fill the screen with black

        # Update the player instance
        updatable.update(dt)  
        # Check for collisions between the player and asteroids

        for asteroid in asteroids:
            if player_object.check_collision(asteroid):
                print("Game Over!")
                pygame.quit()
                running = False
                break

        # Check for collisions between the asteroids and shots
        for shot in shots:
            for asteroid in asteroids:
                # Use the check_collision method from circleshape to check for collisions
                if shot.check_collision(asteroid):
                    print("Shot hit an asteroid!")
                    # Remove the shot and the asteroid
                    shot.kill()
                    new_asteroids = asteroid.split()  # Split the asteroid into smaller ones
                    if new_asteroids:
                        for new_asteroid in new_asteroids:
                            # Add the new asteroids to the group
                            asteroids.add(new_asteroid)
                            drawable.add(new_asteroid)
                            updatable.add(new_asteroid)
                    # Break the loop if a hit is detected
                    break

        # Draw the player instance
        #drawable.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)
        

        

        pygame.display.flip()  # Update the display

        # Limit the frame rate to 60 FPS
        timer.tick(60)


    # Clean up pygame
    pygame.quit()     

if __name__ == "__main__": 
    main()