import pygame
from constants import *
from player import*
from circleshape import*
pygame.init()

def main():
	Clock = pygame.time.Clock()
	dt = 0
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		events = pygame.event.get()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = Clock.tick(60) / 1000
		screen.fill("black")
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()


if __name__ == "__main__": #Ensures the main() is only called when this file is run directly and won't run if it's imported
	main()
