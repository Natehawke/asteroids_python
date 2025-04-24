# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# This is the main file for the asteroids game. It will run the game and handle all the events. 
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display


    

if __name__ == "__main__": 
    main()