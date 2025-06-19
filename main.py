import pygame
from constants import *
pygame.init()

def main():
	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
        		return
	Clock = pygame.time.Clock()
	dt = 0
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		screen.fill("black")
		pygame.display.flip()
		dt = Clock.tick(60) / 1000

if __name__ == "__main__": #Ensures the main() is only called when this file is run directly and won't run if it's imported
	main()
