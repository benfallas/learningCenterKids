
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
font = pygame.font.Font('freesansbold.ttf', 50)


# displaying a window of height
# 500 and width 400
displaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# creating a bool value which checks
# if game is running
running = True
text = font.render("Welcome", True, blue)
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
            #make text larger
            font = pygame.font.Font('freesansbold.ttf', 500)
            if event.key == pygame.K_ESCAPE:
                #If escame key pressed end the game
                running = False
            if event.key == pygame.K_a:
                text = font.render("Aa", True, blue)
            if event.key == pygame.K_b:
                text = font.render("Bb", True, blue)
            if event.key == pygame.K_c:
                text = font.render("Cc", True, blue)
            if event.key == pygame.K_d:
                text = font.render("Dd", True, blue)
            if event.key == pygame.K_e:
                text = font.render("Ee", True, blue)
            if event.key == pygame.K_f:
                text = font.render("Ff", True, blue)
            if event.key == pygame.K_g:
                text = font.render("Gg", True, blue)
            if event.key == pygame.K_h:
                text = font.render("Hh", True, blue)
            if event.key == pygame.K_i:
                text = font.render("Ii", True, blue)
            if event.key == pygame.K_j:
                text = font.render("Jj", True, blue)
            if event.key == pygame.K_k:
                text = font.render("Kk", True, blue)
            if event.key == pygame.K_l:
                text = font.render("Ll", True, blue)
            if event.key == pygame.K_m:
                text = font.render("Mm", True, blue)
            if event.key == pygame.K_n:
                text = font.render("Nn", True, blue)
            if event.key == pygame.K_o:
                text = font.render("Oo", True, blue)
            if event.key == pygame.K_p:
                text = font.render("Pp", True, blue)
            if event.key == pygame.K_q:
                text = font.render("Qq", True, blue)
            if event.key == pygame.K_r:
                text = font.render("Rr", True, blue)
            if event.key == pygame.K_s:
                text = font.render("Ss", True, blue)
            if event.key == pygame.K_t:
                text = font.render("Tt", True, blue)
            if event.key == pygame.K_u:
                text = font.render("Uu", True, blue)
            if event.key == pygame.K_v:
                text = font.render("Vv", True, blue)
            if event.key == pygame.K_w:
                text = font.render("Ww", True, blue)
            if event.key == pygame.K_x:
                text = font.render("Xx", True, blue)
            if event.key == pygame.K_y:
                text = font.render("Yy", True, blue)
            if event.key == pygame.K_z:
                text = font.render("Zz", True, blue)

            textRect = text.get_rect()
            textRect.midright = (screenWidth / 2, screenHeight / 2)
