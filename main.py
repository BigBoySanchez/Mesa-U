import pygame
import game_config
from make_emails import make_emails


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
    screen.blit(start_text, (25, 25))

    # Begin Button
    begin_button_width = 200
    begin_button_height = 50
    begin_button_x = 540
    begin_button_y = 510
    begin_button = pygame.Surface((begin_button_width, begin_button_height))
    begin_button_image = pygame.image.load("./images/login-btn.png")
    begin_button_rect = pygame.Rect((begin_button_x, begin_button_y, begin_button_width, begin_button_height))
    # begin_button.fill("white")

    begin_button_font = pygame.font.Font(None, 35)
    begin_button_text = begin_button_font.render("Start", True, (0, 0, 0))

    begin_button.blit(begin_button_text, (71, 15))

    # help menu button
    help_menu_button = pygame.Surface((200, 50))
    help_menu_button.fill((200, 200, 200))
    help_menu_button_rect = pygame.Rect((25, 605, 200, 50)) # coordinates first, hitbox second
    help_menu_button_font = pygame.font.Font(None, 35)
    help_menu_button_text = help_menu_button_font.render("Help", True, (0, 0, 0))
    help_menu_button.blit(help_menu_button_text, (72, 12))

    screen.blit(help_menu_button, help_menu_button_rect)
    # Start button
    bluescreen_button_rect = pygame.draw.rect(screen, (0, 255, 0), [1200, 600, begin_button_width, begin_button_height])

    screen.blit(begin_button, begin_button_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_config.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if begin_button_rect.collidepoint(pos):
                # goto next screen
                game_config.initial_page_load = False
                game_config.email_page_load = True
            elif bluescreen_button_rect.collidepoint(pos):
                game_config.initial_page_load = False
                game_config.blue_screen_page_load = True
            elif help_menu_button_rect.collidepoint(pos):
                game_config.initial_page_load = False
                game_config.help_screen_page_load = True

    # for event in pygame.event.get():
    #    if green_button.get_rect().collidepoint(pos):
    #        print("Button Clicked")





def email_page(screen):
    # Globals
    global running
    global initial_page_load
    global email_page_load
    
    WIDTH, HEIGHT = screen.get_size()

    screen.fill("white")
    pygame.display.flip()

    # Background image
    bg_image = pygame.image.load("./images/email-bg.png")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))
    screen.blit(bg_image, (0,0))

    # Back button
    back_button_width = 30
    back_button_height = 30

    back_button = pygame.Surface((back_button_width, back_button_height))
    back_button.fill((125, 95, 125))
    back_button_rect = pygame.Rect((1230 - 5, 5, back_button_width, back_button_height))
    back_button_font = pygame.font.Font(None, 35)

    back_button_text = back_button_font.render("B", True, (0, 0, 0))
    back_button.blit(back_button_text, (5, 4))

    screen.blit(back_button, back_button_rect.topleft)

    # email buttons

    email_rect = pygame.Rect(0, 0, WIDTH * 0.2488, HEIGHT / 2.89)
    
    # WIP: might delete later
    # email1 = pygame.draw.rect(screen, (0, 0, 255), email_rect)

    # email_rect.y = email1.bottom
    # email2 = pygame.draw.rect(screen, (255, 0, 255), email_rect)

    # email_rect.y = email2.bottom
    # email3 = pygame.draw.rect(screen, (255, 255, 0), email_rect)

    email_rect.y = 0
    email_rect.h = HEIGHT

    # WIP: in case we can't get pfp's
    pygame.draw.rect(screen, (255, 0, 255), [436, 180, 55, 55])

    emails = make_emails(screen)

    # Event loop
    curr_running = True
    while curr_running:
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                curr_running = False
                game_config.running = False

            # Buttons alone
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Back button
                if back_button_rect.collidepoint(pos):
                    print("Going back to start")
                    curr_running = False
                    game_config.initial_page_load = True
                    game_config.email_page_load = False

                # side emails
                if email_rect.collidepoint(pos):
                    email_num = pos[1] // (HEIGHT / 3) + 1
                    print(email_num)
                    to_display = emails[(int)(email_num) - 1]
                    screen.blit(to_display.body, (email_rect.right, HEIGHT / 3))
    
        pygame.display.flip()

def bluescreen(screen):
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
    for x in range(0, game_config.NUM_LIVES):
        if x != 0:
            pygame.draw.line(screen, (0, 0, 0), ((x * infoWidth / game_config.NUM_LIVES) + wholeRect.x, wholeRect.top), ((x * infoWidth / game_config.NUM_LIVES) + wholeRect.x, wholeRect.bottom))
        
        numText = numFont.render((str)(x + 1), True, (0, 0, 0))
        numRect = numText.get_rect(center=(wholeRect.x + ((x + 0.5) * infoWidth / game_config.NUM_LIVES), wholeRect.y + (wholeRect.h / 2)))

        screen.blit(numText, (numRect.left, numRect.top))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_config.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if retry_button_rect.collidepoint(mouse_pos):
                game_config.initial_page_load = True
                game_config.blue_screen_page_load = False


def help_screen(screen):
    screen.fill("Grey")

    lore_font = pygame.font.Font(None, 35)
    lore_text = lore_font.render("As a student of California State University East Bay, it's critical to check your Email regularly!", True, (0, 0, 0))
    screen.blit(lore_text, (10, 20))

    help_font = pygame.font.Font(None, 35)
    help_text = help_font.render("However, there may be scams, phishing attacks, and other dangers.", True, (0, 0, 0))
    screen.blit(help_text, (10, 60))

    help_font_two = pygame.font.Font(None, 35)
    help_text_two = help_font_two.render("Here's a few ways to protect yourself", True, (0, 0, 0))
    screen.blit(help_text_two, (10, 100))
    
    help_font_three = pygame.font.Font(None, 35)
    help_text_three = help_font.render("    1. Double check who sent the email.", True, (0, 0, 0))
    screen.blit(help_text_three, (10, 140))

    help_font_four = pygame.font.Font(None, 35)
    help_text_four = help_font.render("    2. Look out for spelling mistakes.", True, (0, 0, 0))
    screen.blit(help_text_four, (10, 180))

    help_font_five = pygame.font.Font(None, 35)
    help_text_five = help_font.render("    3. Be weary of phrases like \"CRITICALLY IMPORTANT!!\" or \"YOU'RE ACCOUNT HAS BEEN HACKED!\"", True, (0, 0, 0))
    screen.blit(help_text_five, (10, 220))

    help_font_six = pygame.font.Font(None, 35)
    help_text_six = help_font.render("    4. If you notice these things, don't click on any links or download any files.", True, (0, 0, 0))
    screen.blit(help_text_six, (10, 260))

    back_button = pygame.Surface((200, 50))
    back_button.fill((255, 255, 255))
    back_button_rect = pygame.Rect((500, 600, 200, 50))
    back_button_font = pygame.font.Font(None, 35)
    back_button_text = back_button_font.render("Back", True, (0, 0, 0))
    back_button.blit(back_button_text, (72, 12))
    screen.blit(back_button, back_button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_config.running = False


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
        elif game_config.help_screen_page_load:
            help_screen(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
