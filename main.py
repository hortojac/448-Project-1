#Test pygame file
#Import and initialize the pygame library
import pygame
#import sys function to stop the program
from sys import exit

pygame.init()

#Colors (can use RGB or hexadecimal values)
white = (255,255,255)
black = (0,0,0)

#Set up a drawing window 
screen = pygame.display.set_mode([1000,800])

# Run until the user wants to quit
while True:
	#Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
            #exits the game
			exit()
	#fill the background with white
	screen.fill(white)

	#draw a circle
	pygame.draw.circle(screen, (0,0,255), (250,250), 75)
	#draw a rectangle
	pygame.draw.rect(screen, black, pygame.Rect(30,30,60,60))

	# Flip the display (update the contents to the screen)
	pygame.display.flip()
#Done! Time to quit
pygame.quit()

