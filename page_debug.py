import pygame
import game_config
from email import Email

page_load = False
curr_email = -1

# put page to debug here
def email_page(screen):
    # Globals
    global running
    global initial_page_load
    global email_page_load
    
    WIDTH, HEIGHT = screen.get_size()

    screen.fill("white")
    pygame.display.flip()

    # Sample emails
    body_font = pygame.font.Font(None, 100)
    
    legit1_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    legit1_text = body_font.render("lazy ahhhh boy", True, (0, 0, 0))
    legit1_body.blit(legit1_text, (0, 0))

    legit1 = Email("Do your homework!", "Ms. Teacher", "t.cher@gmail.com", legit1_body, "reply", "real teacher")

    evil1_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil1_text = body_font.render("CLICK THE LINK BELOW \\/ \\/ \\/", True, (0, 0, 0))
    evil1_body.blit(evil1_text, (0, 0))

    evil1 = Email("1,000,000 FREE ROBUX!", "Robux Raider", "3yd98@hotmail.to", evil1_body, "report", "malicious link")

    evil2_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil2_text = body_font.render("go to my ig <3 \\/ \\/ \\/", True, (0, 0, 0))
    evil2_body.blit(evil2_text, (0, 0))

    evil2 = Email("i wuv u :3", "Bethany Aberdale", "baberd@yahoo.com", evil2_body, "report", "malicious link")

    emails = [legit1, evil1, evil2]

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
                    game_config.initial_page_load = True
                    game_config.email_page_load = False

                # side emails
                if email_rect.collidepoint(pos):
                    email_num = pos[1] // (HEIGHT / 3) + 1
                    print(email_num)
                    to_display = emails[(int)(email_num) - 1]
                    screen.blit(to_display.body, (email_rect.right, HEIGHT / 3))

    

def initial_page(screen):
    # Grab the needed globals
    global page_load

    # fill the background first, then add stuff later
    screen.fill("white")

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
    begin_button.fill((0, 255, 0))

    begin_button_font = pygame.font.Font(None, 35)
    begin_button_text = begin_button_font.render("Start", True, (0, 0, 0))

    begin_button.blit(begin_button_text, (71, 15))

    # Start button
    begin_button_rect = pygame.Rect((begin_button_x, begin_button_y, begin_button_width, begin_button_height))

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
                page_load = True

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((1270, 700))
    clock = pygame.time.Clock()
    while game_config.running:
        # Fill the screen with blue
        if game_config.initial_page_load:
            initial_page(screen)
        elif page_load:
            # replace me with call to page
            email_page(screen)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()