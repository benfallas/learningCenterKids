
# import pygame package
import pygame
pygame.init()
file = ''
pygame.init()
pygame.mixer.init()

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
image = pygame.image.load('./images/baby').convert() #baby image
image_rect = image.get_rect()
image_rect.center = (screenWidth/2, screenHeight/3 * 1) #default image

# keep game running till running is true
while running:

    #Make the screen white
    displaySurface.fill(white)

    # Draw the text over the rectangle
    displaySurface.blit(text, textRect)
    # Draw the text over the rectangle
    displaySurface.blit(image, image_rect)


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
                pygame.mixer.music.load("./audio/phonics/a.mp3")
                pygame.mixer.music.play()
                text = font.render("Aa", True, blue)
                image = pygame.image.load('./images/apple.jpg').convert()
                image_rect = image.get_rect()
                #image accordering to letter
            if event.key == pygame.K_b:
                pygame.mixer.music.load("./audio/phonics/b.mp3")
                pygame.mixer.music.play()
                text = font.render("Bb", True, blue)
                image = pygame.image.load('./images/ball.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_c:
                pygame.mixer.music.load("./audio/phonics/c.mp3")
                pygame.mixer.music.play()
                text = font.render("Cc", True, blue)
                image = pygame.image.load('./images/cat.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_d:
                pygame.mixer.music.load("./audio/phonics/d.mp3")
                pygame.mixer.music.play()
                text = font.render("Dd", True, blue)
                image = pygame.image.load('./images/dog.webp').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_e:
                pygame.mixer.music.load("./audio/phonics/e.mp3")
                pygame.mixer.music.play()
                text = font.render("Ee", True, blue)
                image = pygame.image.load('./images/elephant.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_f:
                pygame.mixer.music.load("./audio/phonics/f.mp3")
                pygame.mixer.music.play()
                text = font.render("Ff", True, blue)
                image = pygame.image.load('./images/frog.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_g:
                pygame.mixer.music.load("./audio/phonics/g.mp3")
                pygame.mixer.music.play()
                text = font.render("Gg", True, blue)
                image = pygame.image.load('./images/guitar.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_h:
                pygame.mixer.music.load("./audio/phonics/h.mp3")
                pygame.mixer.music.play()
                text = font.render("Hh", True, blue)
                image = pygame.image.load('./images/hat.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_i:
                pygame.mixer.music.load("./audio/phonics/i.mp3")
                pygame.mixer.music.play()
                text = font.render("Ii", True, blue)
                image = pygame.image.load('./images/igloo.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_j:
                pygame.mixer.music.load("./audio/phonics/j.mp3")
                pygame.mixer.music.play()
                text = font.render("Jj", True, blue)
                image = pygame.image.load('./images/jump.webp').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_k:
                pygame.mixer.music.load("./audio/phonics/k.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/kangaroo.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Kk", True, blue)
            if event.key == pygame.K_l:
                pygame.mixer.music.load("./audio/phonics/l.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/lion.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Ll", True, blue)
            if event.key == pygame.K_m:
                pygame.mixer.music.load("./audio/phonics/m.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/monkey.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Mm", True, blue)
            if event.key == pygame.K_n:
                pygame.mixer.music.load("./audio/phonics/n.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/nurse.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Nn", True, blue)
            if event.key == pygame.K_o:
                pygame.mixer.music.load("./audio/phonics/o.mp3")
                pygame.mixer.music.play()
                text = font.render("Oo", True, blue)
                image = pygame.image.load('./images/octopus.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_p:
                pygame.mixer.music.load("./audio/phonics/p.mp3")
                pygame.mixer.music.play()
                text = font.render("Pp", True, blue)
                image = pygame.image.load('./images/pumpkin.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_q:
                pygame.mixer.music.load("./audio/phonics/q.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/queen.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Qq", True, blue)
            if event.key == pygame.K_r:
                pygame.mixer.music.load("./audio/phonics/r.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/rocket.png').convert()
                image_rect = image.get_rect()
                text = font.render("Rr", True, blue)
            if event.key == pygame.K_s:
                pygame.mixer.music.load("./audio/phonics/s.mp3")
                pygame.mixer.music.play()
                text = font.render("Ss", True, blue)
                image = pygame.image.load('./images/snake.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_t:
                pygame.mixer.music.load("./audio/phonics/t.mp3")
                pygame.mixer.music.play()
                text = font.render("Tt", True, blue)
                image = pygame.image.load('./images/train.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_u:
                pygame.mixer.music.load("./audio/phonics/u.mp3")
                pygame.mixer.music.play()
                text = font.render("Uu", True, blue)
                image = pygame.image.load('./images/umbrella.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_v:
                pygame.mixer.music.load("./audio/phonics/v.mp3")
                pygame.mixer.music.play()
                image = pygame.image.load('./images/violin.jpeg').convert()
                image_rect = image.get_rect()
                text = font.render("Vv", True, blue)
            if event.key == pygame.K_w:
                pygame.mixer.music.load("./audio/phonics/w.mp3")
                pygame.mixer.music.play()
                text = font.render("Ww", True, blue)
                image = pygame.image.load('./images/watch.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_x:
                pygame.mixer.music.load("./audio/phonics/x.mp3")
                pygame.mixer.music.play()
                text = font.render("Xx", True, blue)
                image = pygame.image.load('./images/box.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_y:
                pygame.mixer.music.load("./audio/phonics/y.mp3")
                pygame.mixer.music.play()
                text = font.render("Yy", True, blue)
                image = pygame.image.load('./images/yellow.jpeg').convert()
                image_rect = image.get_rect()
            if event.key == pygame.K_z:
                pygame.mixer.music.load("./audio/phonics/z.mp3")
                pygame.mixer.music.play()
                text = font.render("Zz", True, blue)
                image = pygame.image.load('./images/zebra.png').convert()
                image_rect = image.get_rect()

            textRect = text.get_rect()
            textRect.midright = (screenWidth / 2, screenHeight / 2)
            image_rect.center = ((screenWidth / 4) * 3, screenHeight / 2)
