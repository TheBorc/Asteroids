import pygame
import sys
from constants import *
from player import*
from circleshape import*
from asteroidfield import*
from asteroid import*
pygame.init()

def main():
	Clock = pygame.time.Clock()
	dt = 0
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Shot.containers = (updatable, drawable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = Clock.tick(60) / 1000
		screen.fill("black")

		for u in updatable:
			u.update(dt)


		for d in drawable:
			d.draw(screen)

		for a in asteroids:
			a.update(dt)
			if player.collision(a):
				print("Game over!")
				sys.exit()

		pygame.display.flip()


if __name__ == "__main__": #Ensures the main() is only called when this file is run directly and won't run if it's imported
	main()
