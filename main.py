import pygame
import game_config


class Button:
    def __init__(self,x, y, width, height, text="", color="", image=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.image = image


def initial_page(screen):
    # Grab the needed globals
    global running
    global initial_page_load
    global email_page_load
    global blue_screen_page_load

    # fill the background first, then add stuff later
    screen.fill("white")

    # Background image
    bg_image = pygame.image.load("./images/mainmenu-bg.png")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))
    screen.blit(bg_image, (0,0))

    # Main text
    start_font = pygame.font.Font(None, 35)
    start_text = start_font.render("Totally secure email client", True, (0, 0, 0))
    screen.blit(start_text, (450, 100))

    # Begin Button
    begin_button_width = 200
    begin_button_height = 50
    begin_button_x = 550
    begin_button_y = 500
    begin_button = pygame.Surface((begin_button_width, begin_button_height))
    begin_button_image = pygame.image.load("./images/login-btn.png")

    begin_button_font = pygame.font.Font(None, 35)
    begin_button_text = begin_button_font.render("Start", True, (0, 0, 0))

    begin_button.blit(begin_button_text, (71, 15))

    # Start button
    begin_button_rect = pygame.Rect((begin_button_x, begin_button_y, begin_button_width, begin_button_height))
    bluescreen_button_rect = pygame.draw.rect(screen, (0, 255, 0), [30, 30, begin_button_width, begin_button_height])

    screen.blit(begin_button, begin_button_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_config.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if begin_button_rect.collidepoint(pos):
                # goto next screen
                print("butoon clicked")
                game_config.initial_page_load = False
                game_config.email_page_load = True
            elif bluescreen_button_rect.collidepoint(pos):
                print("blue")
                game_config.initial_page_load = False
                game_config.blue_screen_page_load = True

    # for event in pygame.event.get():
    #    if green_button.get_rect().collidepoint(pos):
    #        print("Button Clicked")


def email_page(screen):
    # Globals
    global running
    global initial_page_load
    global email_page_load
    screen.fill("white")

    # Background image
    bg_image = pygame.image.load("./images/email-bg.png")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))
    screen.blit(bg_image, (0,0))

    # Back button
    back_button_width = 30
    back_button_height = 30

    back_button = pygame.Surface((back_button_width, back_button_height))
    back_button.fill((125, 95, 125))
    back_button_rect = pygame.Rect((5, 5, back_button_width, back_button_height))
    back_button_font = pygame.font.Font(None, 35)

    back_button_text = back_button_font.render("B", True, (0, 0, 0))
    back_button.blit(back_button_text, (6, 4))

    screen.blit(back_button, back_button_rect.topleft)

    # Event loop
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            game_config.running = False

        # Buttons alone
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # Back button
            if back_button_rect.collidepoint(pos):
                print("Going back to start")
                game_config.initial_page_load = True
                game_config.email_page_load = False

            # Other buttons

NUM_LIVES = 3
def bluescreen(screen):
    global NUM_LIVES
    WIDTH, HEIGHT = screen.get_size()

    mouse_pos = pygame.mouse.get_pos()

    screen.fill("blue")

    hackFont = pygame.font.Font(None, 220)
    numFont = pygame.font.Font(None, 100)

    sadText = pygame.font.Font(None, 270).render(":(", True, (255, 255, 255))  # Render ":(" in white
    # hackFont.set_bold(True)

    hackTitle = hackFont.render("You got hacked!", True, (255, 255, 255))
    whyText = pygame.font.Font(None, 80).render("Here's why:", True, (255, 255, 255))

    sadRect = sadText.get_rect(topleft=(WIDTH / 32, HEIGHT / 16))
    hackRect = hackTitle.get_rect(topleft=(sadRect.left, sadRect.bottom))
    whyRect = whyText.get_rect(topleft=(hackRect.left, hackRect.bottom))

    screen.blit(sadText, (sadRect.left, sadRect.top))
    screen.blit(hackTitle, (sadRect.left, sadRect.bottom + 30))
    screen.blit(whyText, (hackRect.left, hackRect.bottom + 70))

    retry_button = pygame.Surface((200, 50))
    retry_button.fill((255, 255, 255))
    retry_button_rect = pygame.Rect((600, 600, 200, 50))
    retry_button_font = pygame.font.Font(None, 35)
    retry_button_text = retry_button_font.render("New Game", True, (0, 0, 0))
    retry_button.blit(retry_button_text, (5, 5))

    screen.blit(retry_button, retry_button_rect)
    
    # making the loss info boxes
    infoWidth = WIDTH / 1.5
    wholeRect = pygame.draw.rect(screen, (255, 255, 255), [whyRect.right + 40, whyRect.bottom + 10, infoWidth, 100])
    for x in range(0, NUM_LIVES):
        if x != 0:
            pygame.draw.line(screen, (0, 0, 0), ((x * infoWidth / NUM_LIVES) + wholeRect.x, wholeRect.top), ((x * infoWidth / NUM_LIVES) + wholeRect.x, wholeRect.bottom))
        
        numText = numFont.render((str)(x + 1), True, (0, 0, 0))
        numRect = numText.get_rect(center=(wholeRect.x + ((x + 0.5) * infoWidth / NUM_LIVES), wholeRect.y + (wholeRect.h / 2)))

        screen.blit(numText, (numRect.left, numRect.top))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_config.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if retry_button_rect.collidepoint(mouse_pos):
                game_config.initial_page_load = True
                game_config.blue_screen_page_load = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1270, 700))
    clock = pygame.time.Clock()
    while game_config.running:
        # Fill the screen with blue
        if game_config.initial_page_load:
            initial_page(screen)
        elif game_config.email_page_load:
            email_page(screen)
        elif game_config.blue_screen_page_load:
            bluescreen(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
