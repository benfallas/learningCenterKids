
# import pygame package
import pygame
pygame.init()

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screenWidth = pygame.display.Info().current_w # gets monitor info
screenHeight = pygame.display.Info().current_h # gets monitor info

# initializing imported module
font = pygame.font.Font('freesansbold.ttf', 32)


# displaying a window of height
# 500 and width 400
displaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# creating a bool value which checks
# if game is running
running = True
text = font.render("Welcome", True, green, blue)
textRect = text.get_rect()
textRect.center = (screenWidth / 2, screenHeight / 2)

# keep game running till running is true
while running:

    #Make the screen white
    displaySurface.fill(white)

    # Draw the text over the rectangle
    displaySurface.blit(text, textRect)

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
        # Draws the surface object to the screen.
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #If escame key pressed end the game
                running = False
            if event.key == pygame.K_a:
                text = font.render("A", True, green, blue)
    if event.key == pygame.K_a:
        text = font.render("A", True, green, blue)
