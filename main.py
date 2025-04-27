# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# This is the main file for the asteroids game. It will run the game and handle all the events. 
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    player_object = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

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
        player_object.update(dt)  

        # Draw the player instance
        player_object.draw(screen)

        

        pygame.display.flip()  # Update the display

        # Limit the frame rate to 60 FPS
        timer.tick(60)


    # Clean up pygame
    pygame.quit()     

if __name__ == "__main__": 
    main()